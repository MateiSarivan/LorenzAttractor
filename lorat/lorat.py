import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lorenz

def main(args = None):

    print("Given arguments how: ", args)
    print("ok")

    # Set initial conditions
    
    #x = [0]; y = [1]; z = [1.05]
    #x = [1.]; y = [1.05]; z = [0.]

    # Generate set of system parameters (timestep, length), (dt, N) 
    #dt = 10.0 ** (-1 * np.arange(5))
    #N = 5 * 10 ** np.arange(2,7) #create a folder for each of these
    dt = 0.001
    N = 50000

    sigma = [10, 10, 10, 14, 14]
    betta = [8/3, 8/3, 8/3, 8/3, 13/3]
    ro = [6, 16, 28, 28, 28]

    #x, y, z = lorenz.euler(x, y, z, sigma[0], ro[0], betta[0], dt, N)
    # xarray = np.zeros([N, 5])
    # yarray = np.zeros([N, 5])
    # zarray = np.zeros([N, 5])

    s_total = []
    t_total = []
    u_total = []

    for i in np.arange(len(sigma)):
        
        x = [1.]; y = [1.]; z = [1.]
        s, t, u = lorenz.euler(x, y, z, sigma[i], ro[i], betta[i], dt, N)
        
        s_total.append(s)
        t_total.append(t)
        u_total.append(u)


    #folder directory
    for i in np.arange(len(s_total)):
        graph3D(s_total[i], t_total[i], u_total[i])
        graph2D(s_total[i], t_total[i], u_total[i])
        #dump to folder

    
    plt.show(block=True)

    plt.subplot(131)
    plt.plot(x,y)
    plt.subplot(132)
    plt.plot(y,z)
    plt.subplot(133)
    plt.plot(x,z)