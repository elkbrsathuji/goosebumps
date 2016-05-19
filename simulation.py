import numpy as np
from junction import junction as base_junction
import matlab.engine

import time


def simulate(adj_mat, T = 200):
    junction = base_junction(adj_mat)
    oracle = None
    tf = np.zeros((4,4))
    tf = tf.tolist()
    for t in range(T):
        if t<50:
            junction.tick(t,tf)
            continue
        junction.tick(t,tf)
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


if __name__ == "__main__":
    st = time.time()

    eng = matlab.engine.start_matlab()

    LANES = 4
    adj_mat = np.ones((4,4))-np.identity(4)
    simulate(adj_mat.tolist())
