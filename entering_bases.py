import numpy as np

def entering(bases, demand, column, repl):
    bases[:,repl] = column;
    total_logs_new = np.matmul(np.linalg.pinv(bases), demand);
    #print(total_logs_new)
    return total_logs_new, bases