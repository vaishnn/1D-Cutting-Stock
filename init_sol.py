import math
import numpy as np

def initial_solution(width, total_width):
    bases = np.zeros((len(width),len(width)));
    j = 0;
    for i in range(0, len(width)):
        bases[i][j] = math.floor(total_width/width[i]);
        j += 1;
    return bases;