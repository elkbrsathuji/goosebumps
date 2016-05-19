"""
This class simulates a junction,
which is a collection of lanes
"""
from base_lane import base_lane
class junction(object):

    def __init__(self,lanes_array):
        #initialize lanes
        lanes = [[None for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                if lanes_array[i][j]!=None:
                    lanes[i][j] = base_lane()

    