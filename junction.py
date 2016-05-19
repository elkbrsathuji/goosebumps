"""
This class simulates a junction,
which is a collection of lanes
"""
from base_lane import base_lane
class junction(object):

    def __init__(self,lanes_array,gen_array=None):
        #initialize lanes
        self._lanes = [[None for _ in range(4)] for _ in range(4)]
        self._lights = [[[0,0] for _ in range(4)] for _ in range(4)]
        #This array decices which lane have its own generator
        if gen_array==None:
            self._gen_array = [[1]*4]*4
        else:
            self._gen_array=gen_array
        #indices are saving all the indices which have valid lanes
        self._indices = []
        for i in range(4):
            for j in range(4):
                if lanes_array[i][j]!=0:
                    self._lanes[i][j] = base_lane(0.4)
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
        out_car_lanes = []
        for element in self._indices:
            i=element[0]
            j=element[1]
            if self._gen_array[i][j]==1:
                gen=True
            else:
                gen=False
            if t_lights[i][j]==1:
                cars_out = self._lanes[i][j].tick(time,True,gen)
                if cars_out:
                    out_car_lanes.append(j)
                    self.update_junction_statistics(cars_out.get_time_in_j()) # Erez
                #Setting the correct timers for the traffic lights
                #TL turned from red to green, reset timer
                if t_lights[i][j][0]==0:
                    self._lights[i][j][0]=1
                    self._lights[i][j][1]=0
                #Increase timer
                elif t_lights[i][j][0]==1:
                    self._lights[i][j][1]+=1
            else:
                #TL turned from green to red, reset timer
                self._lanes[i][j].tick(time,False,gen)
                if t_lights[i][j][0]==1:
                    self._lights[i][j][0]=0
                    self._lights[i][j][1]=0
                elif t_lights[i][j][0]==0:
                    self._lights[i][j][1]+=1
        return out_car_lanes

    def get_lights(self):
        return self._lights

    def push_car_to_lane(self,lane_idx):
        i=lane_idx[0]
        j=lane_idx[1]
        self._lanes[i][j].add_car()

    # Erez:
    def update_junction_statistics(self,timeInJunc):
        self._timeInJunc.append(timeInJunc)

    def get_statistics(self):
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

        return meanTime,variance,maxTime,amount


    def get_cars_stats(self,time):
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