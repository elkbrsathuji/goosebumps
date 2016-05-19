import base_generator.base_generator
import gause_generator.gauss_generator
import 

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

	def _pop(self)
		self._cars.pop(0)
		return

	def _push(self,cars):
		self._cars.extend(cars)
		return

	def _time_update(self,green):
		#TODO what happens if car leaves the lane?
		count = 0
		for c in self._cars:
			count += c.get_time_in_j
		self._avg = count/len(self._cars)
		self._sum_waiting = count
		return 

	def tick(self, time, green = False):
		self._generate(time)
		self._time_update(green)
		if green:
			self._pop()
		return

