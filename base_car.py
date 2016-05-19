class base_car(object):
    def _init_(self,time):
        """
        Basic car object
        :param time:
        :return:
        """
        self._time_in = time
        self._time_out = -1

    def get_time_in(self):
        return  self._time_in

    def get_time_out(self):
        return self._time_out

    def get_time_in_j(self,time):
        return (time-self._time_in)

    def set_time_out(self,time):
        self._time_out = time

    
