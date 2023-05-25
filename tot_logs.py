import numpy as np

def total_logs(bases, width, demand):
    N_a = np.array([])
    for i in range(0, len(width)):
        N_a = np.append(N_a, demand[i]/bases[i][i])
    N = np.sum(N_a)
    return N_a, N