## Important Libraries
import numpy as np
import math
import os
from inputs import *
from init_sol import *
from tot_logs import *
from rearrange import *
from branch_and_bound import *
from entering_bases import *
from optimal_sol import *

## To clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

## Function to take inputs from the user
width, demand, total_width = inputs()

## Assuming an Initial Solution
bases = initial_solution(width, total_width);
print("Bases = ")
print(bases)


N_a, N = total_logs(bases, demand)
c_b = np.ones(len(width))
print("Total log")
print(N_a)
print("Total logs {}".format(N))

## To calculate the dual variables
Y = np.matmul(c_b,np.linalg.inv(bases))
print("Dual variables")
print(Y)

## Calculating ratios 
ratios = Y/width;
print("Ratios")
print(ratios)

ratios_sorted = np.sort(ratios)[::-1];
print("Ratios sorted")
print(ratios_sorted)



new_width, new_Y, indexing = rearrange(ratios,ratios_sorted,width,Y);
print(new_width)
print(new_Y)    

## To apply branch and bound to get the integer column

optimal_bases, new_total_logs = optimal_sol(bases, new_width, new_Y, total_width,demand, indexing)
print("Optimal Bases")
print(optimal_bases)
print(new_total_logs);