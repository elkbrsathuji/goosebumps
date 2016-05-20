import numpy as np
from junction import junction as base_junction
import matlab.engine

import time


def update_waiting_list(junctions_on_hold, junctionsMeta):
    junctions_on_holdNew = sorted(junctions_on_hold, key=lambda param: param[0])
    junctions_on_hold= []
    for (dist, juncId ,laneIn) in junctions_on_holdNew:
        if dist>0:
            junctions_on_hold.append((dist-1, juncId ,laneIn))
            continue
        prob= np.random.uniform
                
        junctionTo=laneIn+2 % 4
        if prob<0.2:
            junctionTo= laneIn-1 %4
        elif prob>0.8:
            junctionTo= laneIn+1 %4
        junctionsMeta[juncId][0].push_car_to_lane([laneIn, junctionTo])


def simulate(junctionsMeta, T = 200):
    
    oracle = None    
    junctions_on_hold=[] # [(dist,id,laneIn),...]
    
    tf = np.zeros((4,4))
    tf = tf.tolist()
    for t in range(T):
        if junctions_on_hold: #update waiting list
            junctions_on_hold = update_waiting_list(junctions_on_hold, junctionsMeta)

        
        for junction,nei in junctionsMeta:
            
            if t<50:
                junction.tick(t,tf)
                continue
            out_car_lanes= junction.tick(t,tf)
            print nei
            if out_car_lanes:
                for lane in out_car_lanes:
                    if nei:
                        neighbour= [(dist,nID) for nID,lane,dist in nei]
                        if neighbour:
                            junctions_on_hold.append((neighbour[0][0],neighbour[0][1],getMirrrorLane(lane)))
                
            stats = junction.get_cars_stats(t)
            tl = junction.get_lights()
            # if stats==None:
            #     stats=[[0]*4]*4
            for i in range(4):
                for j in range(4):
                    if stats[i][j]==None:
                        stats[i][j]=[0]
            #print "stats",stats
            result=get_entering_cars_number(junction, nei, junctionsMeta,t)
            tf = eng.yahav_main(stats,result)
            print "t=",t
            
    return
    
    
def getMirrrorLane( lane ):
    return (lane+2)%4

def udpate_mat(adj_mat,out):
    
    for i in range(4):
        adj_mat[i][out]=0
        
    return adj_mat


def create_junctions():
    amountJunctions=2
    junctions=[]
    print "junctions"
    i=0
    LANES = 4
    adj_mat = np.ones((4, 4)) - np.identity(4)
    generator_adj_mat = np.ones((4, 4)) - np.identity(4)
    #nei = []
    nei = [1, 1, 3]  # ID,direction , dist in time ticks
    generator_adj_mat = udpate_mat(generator_adj_mat, 1)  # Adj_mat, out directio
    junctions.append([base_junction(adj_mat, generator_adj_mat), nei])

    i = 1
    LANES = 4
    adj_mat = np.ones((4, 4)) - np.identity(4)
    generator_adj_mat = np.ones((4, 4)) - np.identity(4)
    nei = [0, 3, 3]
    print "nei",nei
    generator_adj_mat = udpate_mat(generator_adj_mat, 3)
    junctions.append([base_junction(adj_mat, generator_adj_mat), nei])

    return junctions
# we need to calculate for each lane in each junction, the number of cars that want to reach this lane
def get_entering_cars_number(current_junction, nei, junctionsMeta,t):
    sum = 0
    result = [[[0, 0], [0, 0], [0, 0], [0, 0]]]*4

    neiItem= nei
    neighborID=neiItem[0]

    neignorLane= neiItem[1]

    neighbor= junctionsMeta[neighborID][0]
    neighbor_lights = neighbor.get_lights();  # 4x4 array of pair (boolean light state, time in this state)
    neighbor_stats = neighbor.get_cars_stats(t);  # 4x4 array - on each entry there is a list of numbers (that represent time that each car on this lane alredy waits)


    relevant_lane =  neignorLane#get_relevant_lane(junction_id, neighbor.get_id())
    neighbor_exit_lane = neignorLane+2% 4#get_ne3ighbor_exit_lane(junction_id, neighbor.get_id())
    for i in xrange(4):
        result[relevant_lane][i][1] = neiItem[2]# get_distance(junction_id, neighbor.get_id())
        if neighbor_lights[i][neighbor_exit_lane]:
            sum =+ len(neighbor_stats[i][neighbor_exit_lane])
    for i in xrange(4):
        result[relevant_lane][i][0] = sum*current_junction.get_prob(relevant_lane,i)
    sum = 0
    return result





if __name__ == "__main__":
    st = time.time()

    eng = matlab.engine.start_matlab()
 
    junctions= create_junctions()
    simulate(junctions)
