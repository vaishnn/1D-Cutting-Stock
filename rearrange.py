import numpy as np

def rearrange(ratios,ratios_sorted,width,Y):
    new_width = np.array([])
    new_Y = np.array([])
    for i in range(len(ratios_sorted)):
        index_array = np.where(ratios == ratios_sorted[i])[0]
        if len(index_array) > 1:
            index = int(index_array[0])
        else:
            index = int(index_array)
        ratios[index] = -99
        new_Y = np.append(new_Y,Y[index]);
        new_width = np.append(new_width,width[index]);
    
    return new_width,new_Y;