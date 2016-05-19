"""
This generator generates cars
Its generates with uniform dictibution
"""
from base_car import base_car
import numpy as np


class base_generator(object):
    def __init__(self,prob=0):
        self._prob = prob

    def generate_car(self,time):
        x = np.random.random_sample()
        cars_list = []
        if x<=self._prob:
            car = base_car(time)
            cars_list.append(car)
        return cars_list


