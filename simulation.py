import numpy as np
from junction import junction


def simulate(adj_mat, T = 100):
	junction = base_junction(adj_mat)
	oracle = None    
	TL = np.zeros(4,4)
	TL = TL.tolist()
    for t in xrange(T):
    	junction.tick(t)
    	stats = junction.get_stats()
    	print stats[1:3]
    return



if __name__ == "__main__":
	LANES = 4
    adj_mat = np.ones((4,4))-np.identity(4)
	simulate(adj_mat.tolist())    
