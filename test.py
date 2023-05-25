from branch_and_bound import *
n_width = np.array([10,6,9])
n_Y = np.array([1,0.333,0.5])
total_width = 19
indexing = np.array([2,0,1])
x = branch_and_bounds(n_width,n_Y,total_width,indexing)
print(x)