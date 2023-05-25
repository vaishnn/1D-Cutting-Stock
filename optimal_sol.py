from entering_bases import *
from branch_and_bound import *
from rearrange import *
from tot_logs import *

def optimal_sol(bases, new_width,new_Y,total_width,demand, indexing):
    removed = 2
    gar = 1
    new_total_logs = total_logs(bases,demand)
    while True:
        new_p = branch_and_bounds(new_width,new_Y,total_width,indexing)
        try:
            if new_p == -99:
                print("Opimal solution reached")
                return bases, new_total_logs
        except Exception:
            pass
        new_total_logs,bases = entering(bases, demand, new_p, removed)
        c_b = np.ones(len(new_total_logs))
        Y = np.matmul(c_b,np.linalg.inv(bases))
        print("Dual variables")
        print(Y)

        ## Calculating ratios 
        ratios = Y/new_width;
        print("Ratios")
        print(ratios)
        ratios_sorted = np.sort(ratios)[::-1];
        new_width, new_Y = rearrange(ratios,ratios_sorted,new_width,Y);
        if gar == 1:
            removed -= 1;
        if removed == -1 or gar == 0:
            removed += 1
            gar = 0;