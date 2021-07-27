import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lorat import lorenz
from lorat import plotting

def main(args = None):

    print("Given arguments how: ", args)
    print("ok")

    # Set initial conditions
    
    #x = [0]; y = [1]; z = [1.05]
    #x = [1.]; y = [1.05]; z = [0.]

    # Generate set of system parameters (timestep, length), (dt, N) 
    dt = 10.0 ** (-1 * np.arange(2, 4))
    N = 5 * 10 ** np.arange(3, 5)
    
    sigma = [10, 10, 10, 14, 14]
    beta = [8/3, 8/3, 8/3, 8/3, 13/3]
    beta_str = ["8/3", "8/3", "8/3", "8/3", "13/3"] #generate string to be able to show ratio
    ro = [6, 16, 28, 28, 28]
    
    # Generate solutions for all values of sigma, beta, and ro for (x, y, z) with given dt and N
    solution_space = []

    for j in range(len(dt)):
        s_total = []
        t_total = []
        u_total = []

        for i in np.arange(len(sigma)):
            
            x = [1.]; y = [1.]; z = [1.]
            s, t, u = lorenz.euler(x, y, z, sigma[i], beta[i], ro[i], dt[j], N[j])
            
            s_total.append(s)
            t_total.append(t)
            u_total.append(u)
            pack = [s_total, t_total, u_total, dt[j], N[j]]

        solution_space.append(pack)
    
    #plotting.graph(solution_space[0][0][i], solution_space[0][1][i], solution_space[0][2][i], solution_space[0][3], solution_space[0][4], sigma[0], beta_str[0], ro[0])
    
    # Generate plots for each group of data (x, y, z) depending on (sigma, beta, ro) and (dt, N)
    plot_no = 1
    for solution in solution_space:
        for i in range(len(solution[2])):
            print("Plot:   ", plot_no, "  :")
            print("dt:   ", solution[3], "    N:  ", solution[4])
            plotting.graph(solution[0][i], solution[1][i], solution[2][i], solution[3], solution[4], sigma[i], beta[i], ro[i])
            plot_no += 1
        print("\n")            
    
    plt.show(block=True)