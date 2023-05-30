from entering_bases import *
from branch_and_bound import *
from rearrange import *
from tot_logs import *
from leaving_col import leaving_index

def optimal_sol(bases, new_width,new_Y,total_width,demand, width,Y):
    new_total_logs,tot = total_logs(bases,demand)
    print(tot);
    new_p = np.array([])
    while True:
        new_p = branch_and_bounds(new_width,new_Y,total_width,width,Y)
        try:
            if new_p == 0:
                print("Opimal solution reached")
                return bases, new_total_logs
        except Exception:
            pass
        removed = leaving_index(bases, new_p, new_total_logs)
        #print(removed)
        new_total_logs,bases = entering(bases, demand, new_p, removed)
        print(bases)
        print("Total Logs{}".format(new_total_logs))
        c_b = np.ones(len(new_total_logs))
        Y = np.matmul(c_b,np.linalg.pinv(bases))
        ## Calculating ratios 
        ratios = Y/new_width;
        ratios_sorted = np.sort(ratios)[::-1];
        new_width, new_Y,_ = rearrange(ratios,ratios_sorted,new_width,Y);