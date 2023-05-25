import math
import numpy as np
def branch_and_bounds(new_width,new_Y,total_width):
    x = np.zeros(len(new_width))
    
    x[0] = total_width/new_width[0]
    for i in range(len(new_width)+1):
        #print(x)
        z = np.sum(x*new_Y)
        z_arr = np.array([])
        x_new = np.array([])
        gar_val = math.floor(x[i])
        for j in range(math.floor(x[i])+1):
            if i + 1 == len(new_width):
                  return x;   
            #print(math.floor(x[i]))
            x[i] = j;
            #print(x)
            
            x_new = np.append(x_new,(total_width - np.sum(x*new_width))/new_width[i+1])
            #print(np.sum(x*new_width))
            #print(x_new)
            x[i+1] = x_new[j]
            #print(x)
            z_arr = np.append(z_arr,np.sum(x*new_Y))
            x[i+1] = 0
            #print(z_arr)
            if j == gar_val:
              #print(z_arr)
              x[i] = np.arange(0,gar_val + 1)[z_arr.tolist().index(np.max(z_arr))]
              x[i+1] = x_new[z_arr.tolist().index(np.max(z_arr))]
              print(x)
              