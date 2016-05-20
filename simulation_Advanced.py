import numpy as np
from junction import junction as base_junction
import matlab.engine

import time


def update_waiting_list(junction_on_hold):
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
                
        junctionMeta[juncId][0].push_car_to_lane([laneIn, junctionTo])


def simulate(junctionsMeta, T = 200):
    
    oracle = None    
    junctions_on_hold=[] # [(dist,id,laneIn),...]
    
    tf = np.zeros((4,4))
    tf = tf.tolist()
    for t in range(T):
        if junctions_on_hold:
        junction_on_hold = update_waiting_list(junctions_on_hold)
        if junctions_on_hold: #update waiting list
                        
        
        for junction,nei in junctionsMeta:
            
            if t<50:
                junction.tick(t,tf)
                continue
            out_car_lanes= junction.tick(t,tf)
            
            if out_car_lanes:
                for lane in out_car_lanes:
                    neighbour= [(dist,nID) for nID,lane,dist in nei]
                    if neighbourID:
                        junctions_on_hold.append((neighbour[0][0],neighbour[0][1],getMirrorLane(lane)))
                
            stats = junction.get_cars_stats(t)
    
            # if stats==None:
            #     stats=[[0]*4]*4
            for i in range(4):
                for j in range(4):
                    if stats[i][j]==None:
                        stats[i][j]=[0]
            print "stats",stats	
            tf = eng.yahav_main(stats)
            print "t=",t
            
    return
    
    
def getMirrrorLane( lane ):
    return (lane+2)%4

def udpate_mat(adj_mat,out):
    
    for i in range(4):
        adj_mat[i][out]=0
        
    return adj_mat


def create_junctions(adj_mat):
    amountJunctions=2
    junctions=[]
    for i in range(amoutJunctions):
        LANES = 4
        adj_mat = np.ones((4,4))-np.identity(4)
        generator_adj_mat = np.ones((4,4))-np.identity(4)
        nei=[]
        if i==1:
                nei=nei.append([1,1,3]) #ID,direction , dist in time ticks
                generator_adj_mat= udpate_mat(generator_adj_mat,1) # Adj_mat, out direction
        else:
                nei= nei.append([0,3,3])
                generator_adj_mat= udpate_mat(generator_adj_mat,3)
        junctions.append([base_junction(adj_mat,generator_adj_mat), nei])
    return  junctions

if __name__ == "__main__":
    st = time.time()

    eng = matlab.engine.start_matlab()
 
    junctions= create_junctions()
    simulate(junctions)
