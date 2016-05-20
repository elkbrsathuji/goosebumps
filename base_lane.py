from base_generator import base_generator
# import gause_generator.gauss_generator
from base_car import base_car

class base_lane(object):

	def __init__(self, prob = 0.5, generator = None,generateArray=None):
		self._cars = list()
		self._avg = 0
		self._sum_waiting = 0
		if not generator:
			self._generator = base_generator(prob)
			self._nextGen=-1;
		else:
			self._generateArray=generateArray
			self._nextGen=0;
			self._generator = generator

	def num_cars(self):
		return len(self._cars)

	def set_generator(self, gen):
		self._generator = gen
		return

	def get_avg(self):
		return self._avg

	def get_sum(self):
		return self._sum_waiting

	def add_car(self,time):
		car = base_car(time)
		self._push([car])

	def generate(self, time):
			if self._nextGen==-1:
				cars = self._generator.generate_car(time)
				if len(cars):
					self._push(cars)
			else:
				if self._generateArray(self._nextGen):
					car = base_car(time)
					self._push([car])
					self._nextGen= self._nextGen+1
			return

	def _pop(self, time):
		for car in self._cars[0]:
		    car.set_time_out(time)
		car = self._cars.pop(0)
		return car

	def _push(self,cars):
		self._cars.append(cars)
		return

	def _time_update(self,green,time):
		count = 0
		for c in self._cars:
			for car in c:
				count += car.get_time_in_j(time)
		if len(self._cars)== 0:
			self._avg = 0
		else:
			self._avg = count/len(self._cars)
		self._sum_waiting = count
		return 

	def tick(self, time, green = False,gen=True):
		car_out = None
		if green and len(self._cars)!=0:
			car_out = self._pop(time)
		self._time_update(green,time)
		if gen:
			self.generate(time)
		return car_out

	def export(self,time):
		cars_list=[]
		for list in self._cars:
			for car in list:
				cars_list.append(car.get_time_in_j(time))
		#cars_list = [(car.get_time_in_j(time)) for car in cars]
		if cars_list:
			return cars_list
		else:
			return [0]

