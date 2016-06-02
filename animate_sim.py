import numpy as np
from junction import junction as base_junction
import matlab.engine

import time

class anim_sim(object):

    def __init__(self, T):
        self.T = T

    def simulate(self,adj_mat, T=100):
        junction = base_junction(adj_mat)
        oracle = None
        tf = np.zeros((4, 4))
        tf = tf.tolist()
        for t in range(T):

            junction.tick(t, tf)
            stats = junction.get_stats(t)

            if stats == None:
                stats = [[0] * 4] * 4
            for i in range(4):
                for j in range(4):
                    if stats[i][j] == None:
                        stats[i][j] = [0]
            print "stats", stats
            tf = eng.yahav_main(stats)
            print "t=", t

        # print stats[0][1][1:3]
        return


    def activate(self):
        st = time.time()
        print 'shit'
        eng = matlab.engine.start_matlab()
        end = time.time()
        print "tf", end-st

        LANES = 4
        adj_mat = np.ones((4, 4)) - np.identity(4)
        self.simulate(adj_mat.tolist(), self.T)
