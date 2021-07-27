import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import fractions
from lorat import lorenz
from lorat import plotting

def main(args = None):    
    f = open('configuration.json',)
    data = json.load(f)

    # Generate set of system parameters (timestep, length), (dt, N) 
    dt = np.linspace(start = data['configuration']['dt']['max'], stop = data['configuration']['dt']['min'], num = 10)
    N = np.linspace(start = data['configuration']['N']['min'], stop = data['configuration']['N']['max'], num = 10)
    
    sigma = np.float_(data['configuration']['sigma'])
    beta = [float(fractions.Fraction(x)) for x in data['configuration']['beta']] #transform beta to float
    beta_str = data['configuration']['beta'] 
    rho = np.float_(data['configuration']['rho'])
    
    # Generate solutions for all values of sigma, beta, and rho for (x, y, z) with given dt and N
    solution_space = []

    for j in range(len(dt)):
        s_total = []
        t_total = []
        u_total = []

        for i in np.arange(len(sigma)):
            
            x = [1.]; y = [1.]; z = [1.]
            s, t, u = lorenz.euler(x, y, z, sigma[i], beta[i], rho[i], dt[j], N[j])
            
            s_total.append(s)
            t_total.append(t)
            u_total.append(u)
            pack = [s_total, t_total, u_total, dt[j], N[j]]

        solution_space.append(pack)
    
    #plotting.graph(solution_space[0][0][i], solution_space[0][1][i], solution_space[0][2][i], solution_space[0][3], solution_space[0][4], sigma[0], beta_str[0], ro[0], time_elapsed=0, file_name = None)
    
    #Generate plots for each group of data (x, y, z) depending on (sigma, beta, ro) and (dt, N)
    plot_no = 1
    for solution in solution_space:
        for i in range(len(solution[2])):
            print("Plot:   ", plot_no, "  :")
            print("dt:   ", solution[3], "    N:  ", solution[4])
            plotting.graph(solution[0][i], solution[1][i], solution[2][i], solution[3], solution[4], sigma[i], beta[i], rho[i], time_elapsed=0, file_name = None)
            plot_no += 1
        print("\n")            
    
    plt.show(block=True)