
import numpy as np
from base_generator import base_generator as base

class gause_generator(base):
    def __init__(self,prob=0,var=1.0):
        base.__init__(self,prob)
        self._var=var

    def generate_car(self,time):
        #empty list of cars
        cars_list = []
        x=np.random.normal(scale=self._var)
        #Noramilizing x by variance
        x = x/self._var
        if (x+1)>self._prob:
            pass

