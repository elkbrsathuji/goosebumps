"""
This is the class of the basic car
It contains time it
"""
class base_car(object):
    def _init_(self,time):
        """
        Basic car object
        :param time:
        :return:
        """
        self._time_in = time #The time the car got to the junction
        self._time_out = -1 #The time the car got out of junction

    def get_time_in(self):
        return  self._time_in

    def get_time_out(self):
        return self._time_out

    #retunrn the time the car is currently in the jucntion
    def get_time_in_j(self,time):
        return (time-self._time_in)

    def set_time_out(self,time):
        self._time_out = time


