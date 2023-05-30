import numpy as np

def leaving_index(bases, entering,cost):
    p_j = np.matmul(np.linalg.pinv(bases), entering);
    print(p_j)
    theta = np.array([])
    j = 0
    for i in p_j:
        if i == 0:
            theta = np.append(theta, np.inf);
        else:
            theta = np.append(theta, cost[j]/i);
        j = j + 1
    index = int(np.where(theta == np.min(theta))[0])
    return index;