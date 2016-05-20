import numpy as np
from junction import junction as base_junction
from heatmap import stats_to_mat
import matlab.engine

import time
import matplotlib.pyplot as plt


def simulate(adj_mat, T = 100):
    probs = [[0.0,0.2,0.4,0.3],[0.1,0.0,0.5,0.2],[0.6,0.2,0.0,0.3],[0.2,0.6,0.1,0.0]]
    junction1 = base_junction(adj_mat,None,probs)
    junction2 = base_junction(adj_mat,None,probs)
    tf1 = np.zeros((4,4))
    tf1 = tf1.tolist()
    tf2 = np.zeros((4, 4))
    tf2 = tf2.tolist()
    fig1, ax = plt.subplots("111")
    fig2, ax = plt.subplots("112")
    plt.show(block=False)
    for t in range(T):
        if t<20:
            junction1.tick(t,tf1)
            junction2.tick(t,tf2)
            continue
        junction1.tick(t,tf1)
        junction2.tick(t,tf2)
        stats = junction1.get_cars_stats(t)
        lights = junction1.get_lights()
        stats2 = junction1.get_cars_stats(t)
        # if stats==None:
        #     stats=[[0]*4]*4
        for i in range(4):
            for j in range(4):
                if stats[i][j]==None:
                    stats[i][j]=[0]
        print "stats",stats	
        #probs = np.array(probs)
        tf2 = eng.roundRobin(probs,t)
        tf_mat1 = eng.yahav_main(stats,lights)
        for i in range(4):
            for j in range(4):
                tf1[i][j] = tf_mat1[i][j]
        print tf1
        mat1=stats_to_mat(stats)
        mat2=stats_to_mat(stats)
        heatmap1 = ax1.pcolor(mat1, cmap=plt.cm.YlOrRd)
        heatmap2 = ax2.pcolor(mat2, cmap=plt.cm.YlOrRd)
        fig1.canvas.draw()
        fig2.canvas.draw()
        plt.pause(0.0001)
        print "t=",t
    return


if __name__ == "__main__":
    st = time.time()

    eng = matlab.engine.start_matlab()

    LANES = 4
    adj_mat = np.ones((4,4))-np.identity(4)
    simulate(adj_mat.tolist())
