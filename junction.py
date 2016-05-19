"""
This class simulates a junction,
which is a collection of lanes
"""
from base_lane import base_lane
class junction(object):

    def __init__(self,lanes_array):
        #initialize lanes
        self._lanes = [[None for _ in range(4)] for _ in range(4)]
        #indices are saving all the indixes which have valid lanes
        self._indices = []
        for i in range(4):
            for j in range(4):
                if lanes_array[i][j]!=None:
                    self._lanes[i][j] = base_lane()
                    self._indices.append([i,j])

    """
    At each tick we get the lights and we call all lanes
    to generate new cars and release cars
    inputs: time - current time
    t_lights: current status of traffic lights
    """
    def tick(self,time,t_lights):
        for [element] in self._indices:
            i=element[0]
            j=element[1]
            if t_lights[i][j]==1:
                self._lanes[i][j].tick(time,True)
            else:
                self._lanes[i][j].tick(time)

    