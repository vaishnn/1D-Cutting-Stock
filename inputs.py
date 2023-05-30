import numpy as np
import os 

def inputs():
    os.system('cls' if os.name == 'nt' else 'clear')
    width = np.array([])
    demand = np.array([])

    total_width = int(input("Input total length\n"))
    print("Input cuts as zero to stop")
    while True:
        cuts = int(input("Enter the cut\n"))
        if(cuts == 0):
            break
        width = np.append(width,cuts)
        print("Enter the demand of {} cut".format(cuts))
        demands = int(input())
        demand = np.append(demand,demands);
    return width, demand, total_width