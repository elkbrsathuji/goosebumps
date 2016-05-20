import numpy as np
from junction import junction as base_junction
from heatmap import stats_to_mat
import matlab.engine

import time
import matplotlib.pyplot as plt


def simulate(adj_mat, T = 200):
    probs = [[0.0,0.2,0.4,0.3],[0.1,0.0,0.5,0.2],[0.6,0.2,0.0,0.3],[0.2,0.6,0.1,0.0]]
    junction = base_junction(adj_mat,None,probs)
    tf = np.zeros((4,4))
    tf = tf.tolist()
    fig, ax = plt.subplots()
    plt.show(block=False)
    for t in range(T):
    	if t<50:
        	junction.tick(t,tf)
        	continue
    	junction.tick(t,tf)
    	stats = junction.get_cars_stats(t)
       	lights = junction.get_lights()
        # if stats==None:
        #     stats=[[0]*4]*4
        for i in range(4):
            for j in range(4):
                if stats[i][j]==None:
                    stats[i][j]=[0]
        print "stats",stats	
        #probs = np.array(probs)
        tf = eng.roundRobin(probs,t)
        for i in range(4):
        	for j in range(4):
        		tf[i][j]=int(tf[i][j])
        print tf
        mat=stats_to_mat(stats)
        heatmap = ax.pcolor(mat, cmap=plt.cm.YlOrRd)
        fig.canvas.draw()
        print "t=",t
    return


if __name__ == "__main__":
    st = time.time()

    eng = matlab.engine.start_matlab()

    LANES = 4
    adj_mat = np.ones((4,4))-np.identity(4)
    simulate(adj_mat.tolist())
