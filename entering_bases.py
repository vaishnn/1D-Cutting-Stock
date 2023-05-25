import numpy as np

def entering(bases, demand, column, repl):
    bases[:,repl] = column;
    total_logs_new = np.matmul(np.linalg.inv(bases), demand);
    return total_logs_new, bases