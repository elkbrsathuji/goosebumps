import numpy as np
from junction import junction as base_junction
import matlab.engine

import time


def simulate(adj_mat, T = 100):
	junction = base_junction(adj_mat)
	oracle = None    
	TL = np.zeros((4,4))
	TL = TL.tolist()
	for t in xrange(T):
		junction.tick(t,TL)
		stats = junction.get_stats(t)
		#print stats[0][1][1:3]
	return


if __name__ == "__main__":
	
	st = time.time()

	eng = matlab.engine.start_matlab()
	tf = eng.yahav_main(37)
	end = time.time()
	print tf
	#print "tf", end-st

	LANES = 4
	adj_mat = np.ones((4,4))-np.identity(4)
	simulate(adj_mat.tolist())    
