import numpy as np
from junction import junction as base_junction
import matlab.engine

import time


def simulate(adj_mat, T = 100):
    
    scores=[]
    BIBIBIBI=100 # TODO :  BIBI: Add amount params variations 
    for param in range(BIBIBIBI):
        #generateAr= [i%2  for i in range(T)]        
        generateAr= [i%2  for i in range(T)]        
        junction = base_junction(adj_mat, None, generateAr)
        oracle = None
        tf = np.zeros((4,4))
        tf = tf.tolist()        
        
        for t in range(T):
        	
            junction.tick(t,tf)
            stats = junction.get_stats(t)
    
            if stats==None:
                stats=[[0]*4]*4
            for i in range(4):
            	for j in range(4):
            		if stats[i][j]==None:
            			stats[i][j]=[0]
            print "stats",stats	
            tf = eng.yahav_main(stats)
            print "t=",t
            
        scores.append(junction.get_statistics())
        
		#print stats[0][1][1:3]
    return scores


if __name__ == "__main__":
	
    st = time.time()

    eng = matlab.engine.start_matlab()
    #end = time.time()
    #print "tf", end-st

    LANES = 4
    adj_mat = np.ones((4,4))-np.identity(4)
    simulate(adj_mat.tolist())
