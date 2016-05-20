import numpy as np
from junction import junction as base_junction
import matplotlib.pyplot as plt

def simulate(adj_mat, T = 200):
    junction = base_junction(adj_mat)
    oracle = None
    tf = np.zeros((4,4))
    tf = tf.tolist()
    fig, ax = plt.subplots()
    plt.show(block=False)
    for t in range(T):
        #if t<50:
        #    junction.tick(t,tf)
        #    continue
        junction.tick(t,tf)
        stats = junction.get_cars_stats(t)

        # if stats==None:
        #     stats=[[0]*4]*4
        for i in range(4):
            for j in range(4):
                if stats[i][j]==None:
                    stats[i][j]=[0]
        print "stats",stats
        mat=stats_to_mat(stats)
        heatmap = ax.pcolor(mat, cmap=plt.cm.YlOrRd)
        fig.canvas.draw()
        print "t=",t
    return

def stats_to_mat(stats):
    mat = np.zeros((47,47),dtype=int)
    #Generating lane 0
    for i in range(np.min((len(stats[0][1]),20))):
        mat[26+i][25]=stats[0][1][i]
        mat[26+i][26]=stats[0][1][i]
    for i in range(np.min((len(stats[0][2]),20))):
        mat[26+i][22]=stats[0][2][i]
        mat[26+i][23]=stats[0][2][i]
        mat[26+i][24]=stats[0][2][i]
    for i in range(np.min((len(stats[0][3]),20))):
        mat[26+i][20]=stats[0][3][i]
        mat[26+i][21]=stats[0][3][i]
    #Generating lane 1
    for i in range(np.min((len(stats[1][0]),20))):
        mat[20][26+i]=stats[1][0][i]
        mat[21][26+i]=stats[1][0][i]
    for i in range(np.min((len(stats[1][3]),20))):
        mat[22][26+i]=stats[1][3][i]
        mat[23][26+i]=stats[1][3][i]
        mat[24][26+i]=stats[1][3][i]
    for i in range(np.min((len(stats[1][2]),20))):
        mat[25][26+i]=stats[1][2][i]
        mat[26][26+i]=stats[1][2][i]
    #Generating lane 2
    for i in range(np.min((len(stats[2][1]),20))):
        mat[20-i-1][26]=stats[2][1][i]
        mat[20-i-1][25]=stats[2][1][i]
    for i in range(np.min((len(stats[2][0]),20))):
        mat[20-i-1][24]=stats[2][0][i]
        mat[20-i-1][23]=stats[2][0][i]
        mat[20-i-1][22]=stats[2][0][i]
    for i in range(np.min((len(stats[2][3]),20))):
        mat[20-i-1][21]=stats[2][3][i]
        mat[20-i-1][20]=stats[2][3][i]
    #Generating lane 3
    for i in range(np.min((len(stats[3][0]),20))):
        mat[26][20-i-1]=stats[3][0][i]
        mat[25][20-i-1]=stats[3][0][i]
    for i in range(np.min((len(stats[3][1]),20))):
        mat[24][20-i-1]=stats[3][1][i]
        mat[23][20-i-1]=stats[3][1][i]
        mat[22][20-i-1]=stats[3][1][i]
    for i in range(np.min((len(stats[3][2]),20))):
        mat[21][20-i-1]=stats[3][2][i]
        mat[20][20-i-1]=stats[3][2][i]
    return mat


if __name__ == "__main__":
    LANES = 4
    adj_mat = np.ones((4,4))-np.identity(4)
    simulate(adj_mat.tolist())
