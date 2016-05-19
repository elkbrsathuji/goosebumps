import base_generator.base_generator
import gause_generator.gauss_generator
import base_car.base_car

class base_lane(object):

	def __init__(self, generator = None):
		self._cars = list()
		self._avg = 0
		self._sum_waiting = 0
		if not generator:
			self._generator = base_generator()
		else:
			self._generator = generator

	def num_cars(self):
		return len(self._cars)

	def set_generator(self, gen):
		self._generator = gen
		return

	def get_avg(self):
		return self._avg

	def get_sum(self);
		return self.sum_waiting

	def _generate(self, time):
		cars = self._generator.generate_car(time)
		if len(cars):
			push(cars)
		return

	def generate(self, time):
		cars = self._generator.generate_car(time)
		if len(cars):
			push(cars)
		return

	def _pop(self, time)
		self._cars[0].set_time_out(time)
		car = self._cars.pop(0)
		return car

	def _push(self,cars):
		self._cars.extend(cars)
		return

	def _time_update(self,green):
		count = 0
		for c in self._cars:
			count += c.get_time_in_j
		self._avg = count/len(self._cars)
		self._sum_waiting = count
		return 

	def tick(self, time, green = False):
		car_out = None
		if green:
			car_out = self._pop(time)
		self._time_update(green)
		self._generate(time)
		return car_out

