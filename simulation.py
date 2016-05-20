import numpy as np
from junction import junction as base_junction
from heatmap import stats_to_mat
import matlab.engine

import time
import matplotlib.pyplot as plt


def simulate(adj_mat, T = 200):
    probs_real = [[0.0,0.1,0.2,0.15],[0.05,0.0,0.25,0.1],[0.3,0.1,0.0,0.15],[0.1,0.3,0.05,0.0]]
    probs = [[0.0,0.08,0.15,0.2],[0.1,0.0,0.20,0.8],[0.1,0.3,0.0,0.25],[0.05,0.2,0.15,0.0]]
    junction1 = base_junction(adj_mat,None,probs_real)
    junction2 = base_junction(adj_mat,None,probs_real)
    tf1 = np.zeros((4,4))
    tf1 = tf1.tolist()
    tf2 = np.zeros((4, 4))
    tf2 = tf2.tolist()
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    plt.show(block=False)
    for t in range(T):
        if t<20:
            junction1.tick(t,tf1)
            junction2.tick(t,tf2)
            continue
        junction1.tick(t,tf1)
        junction2.tick(t,tf2)
        #Statistics
        stats = junction1.get_cars_stats(t)
        mean1 = junction1.get_statistics()[0]
        sum1 = junction1.get_statistics()[3]
        lights = junction1.get_lights()
        stats2 = junction2.get_cars_stats(t)
        mean2 = junction2.get_statistics()[0]
        sum2 = junction2.get_statistics()[3]
        print mean1,sum1
        print "ddd" ,mean2,sum2
        # if stats==None:
        #     stats=[[0]*4]*4
        for i in range(4):
            for j in range(4):
                if stats[i][j]==None:
                    stats[i][j]=[0]
        #print "stats",stats
        #probs = np.array(probs)
        tf2 = eng.roundRobin(probs,t)
        tf_mat1 = eng.yahav_main(stats,lights)
        #print stats
        for i in range(4):
            for j in range(4):
                tf1[i][j] = tf_mat1[i][j]
        #print tf1
        mat1=stats_to_mat(stats)
        mat2=stats_to_mat(stats2)
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
