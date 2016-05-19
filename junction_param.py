"""
This class simulates a junction,
which is a collection of lanes
"""
from base_lane import base_lane
class junction_prm(object):

    def __init__(self,lanes_array,generateArray=[]):
        #initialize lanes
        self._lanes = [[None for _ in range(4)] for _ in range(4)]
        #indices are saving all the indixes which have valid lanes
        self._indices = []
        for i in range(4):
            for j in range(4):
                if lanes_array[i][j]!=0:
                    self._lanes[i][j] = base_lane(0.4,None, generateArray)
                    self._indices.append([i,j])
        print self._indices
        
        self._timeInJunc= []
        
        
    """
    At each tick we get the lights and we call all lanes
    to generate new cars and release cars
    inputs: time - current time
    t_lights: current status of traffic lights
    """
    def tick(self,time,t_lights):
        #Saving an array of lanes which took out cars
        out_car_lanes = [[None for _ in range(4)] for _ in range(4)]
        for element in self._indices:
            i=element[0]
            j=element[1]
            if t_lights[i][j]==1:
                cars_out = self._lanes[i][j].tick(time,True)

                if cars_out:
                    out_car_lanes[i][j]=1
                    self.update_junction_statistics(cars_out.get_time_in_j()) # Erez

            else:
                self._lanes[i][j].tick(time)
        return out_car_lanes

    # Erez:
    def update_junction_statistics(self,timeInJunc):
        self._timeInJunc.append(timeInJunc)


    def getStatistics(self):
        meanTime=0
        maxTime=0
        amount=0
        for timeInJunc in self._timeInJunc:
            meanTime= timeInJunc+meanTime
            amount+=1
            if maxTime<timeInJunc:
                maxTime=timeInJunc

        variance=0
        for timeInJunc in self._timeInJunc:
            variance=(meanTime-timeInJunc)*(meanTime-timeInJunc)/amount
        
        self._timeInJunc.sort()
        median= self._timeInJunc.index[amount/2 + amount%2]
        return meanTime,variance,median, maxTime, amount





    def get_stats(self,time):
        stats = [[None for _ in range(4)] for _ in range(4)]
        for element in self._indices:
            i=element[0]
            j=element[1]
            stats[i][j]=self._get_stats_from_lane(i,j,time)
            #print stats[i][j][1:4]
        return stats

    """
    This function returns 4 elemnts which are a list of cars and their current waiting time
    the average time thier waiting
    the sum of all cars waiting time
    and the number of cars
    """
    def _get_stats_from_lane(self,i,j,time):
        cars = self._lanes[i][j].export(time)
        #print "cars are",cars
        #avg = self._lanes[i][j].get_avg()
        #sum = self._lanes[i][j].get_sum()
        #num_of_cars = self._lanes[i][j].num_cars()
        return cars