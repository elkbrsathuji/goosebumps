import base_generator.base_generator
import gause_generator.gauss_generator

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

	def _generate(self):
		cars = self._generator.generate_car()
		if len(cars):
			push(cars)
		return

	def _pop(self)
		self._cars.pop(0)
		return

	def _push(self,cars):
		self._cars.extend(cars)
		return

	def _avg_update(self):

		pass

	def _sum_update(self):

		pass

	def tick(self, green = False):
		self._generate()
		self._avg_update(green)
		self._sum_update(green)
		return

