import numpy as np

def total_logs(bases, demand):
    N_array = np.matmul(np.linalg.inv(bases), demand);
    N = np.sum(N_array)
    return N_array, N