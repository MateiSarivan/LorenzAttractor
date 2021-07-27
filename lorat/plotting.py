import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def graph(x, y, z, dt, N, sigma, beta, ro, time_elapsed, file_name = None):

    """
    Generates 3D and 2D plots of the Lorenz attractor.

    Parameters
    -------
    x : List of float
        List of x coordinates of the Lorenz attractor.
    y : List of float
        List of y coordinates of the Lorenz attractor.
    z : List of float
        List of z coordinates of the Lorenz attractor.

    dt: Float, optional
        Iteration step. Example value: 0.01.
    N: Float, optional
        Length of iteration. Example value: 50000.
    sigma: Float
        Value of sigma. Example values: 10, or 14.    
    beta: Float
        Value of beta. Example values: 8/3 or 13/3.
    ro: Float
        Value of ro. Example values: 6, 16, or 28.
    time_elapsed: Float
        Time elapsed for solving the Lorenz attractor
    file_name: None, optional
        The name of the file when saved.

    """
    
    # Set figure font   
    font = {'family' : 'Arial',
            'size' : '11'}
    plt.rc('font', **font)

    # Create figure and divide it in sections for 3D and 2D plots
    fig = plt.figure(figsize = (10, 8))
    fig.set_tight_layout(True)
    gs = fig.add_gridspec(ncols=7, nrows=3, wspace=1, hspace = 0.5)
    
    graph3D = fig.add_subplot(gs[0:, :3], projection='3d')
    xy = fig.add_subplot(gs[0, 4:])
    yz = fig.add_subplot(gs[1, 4:])
    xz = fig.add_subplot(gs[2, 4:])
    
    # Determine euclidian distance from one step to the other
    eucled_3D = 0
    eucled_xy = 0
    eucled_yz = 0
    eucled_xz = 0
    
    set_3D = []
    set_xy = []
    set_yz = []
    set_xz = []

    for i in range(0,N-1,1):
        eucled_3D_nu = np.sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2 + (z[i+1] - z[i])**2)
        eucled_xy_nu = np.sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
        eucled_yz_nu = np.sqrt((y[i+1] - y[i])**2 + (z[i+1] - z[i])**2)
        eucled_xz_nu = np.sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
        
        set_3D.append(eucled_3D_nu)
        set_xy.append(eucled_xy_nu)
        set_yz.append(eucled_yz_nu)
        set_xz.append(eucled_xz_nu)

        if eucled_3D_nu > eucled_3D:
            eucled_3D = eucled_3D_nu
        if eucled_xy_nu > eucled_xy:
            eucled_xy = eucled_xy_nu
        if eucled_yz_nu > eucled_xy:
            eucled_yz = eucled_yz_nu
        if eucled_xz_nu > eucled_xz:
            eucled_xz = eucled_xz_nu

    #print("Euclidian distance is: ", eucled_3D)    

    # Add data to figure
    s=10
    cmap = plt.cm.viridis
    for i in range(0,N-s,s):
        eucled_3D_nu = np.sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2 + (z[i+1] - z[i])**2)
        eucled_xy_nu = np.sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
        eucled_yz_nu = np.sqrt((y[i+1] - y[i])**2 + (z[i+1] - z[i])**2)
        eucled_xz_nu = np.sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
        
        graph3D.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=cmap(eucled_3D_nu/eucled_3D), alpha=0.4)
        xy.plot(x[i:i+s+1], y[i:i+s+1], color=cmap(eucled_xy_nu/eucled_xy), alpha=0.4)
        yz.plot(y[i:i+s+1], z[i:i+s+1], color=cmap(eucled_yz_nu/eucled_yz), alpha=0.4)
        xz.plot(x[i:i+s+1], z[i:i+s+1], color=cmap(eucled_xz_nu/eucled_xz), alpha=0.4)

    # Customize 3D plot
    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(np.min(set_3D), np.max(set_3D)), cmap=cmap), ax=graph3D, orientation = 'horizontal', label='Euclidian distance')
    graph3D.set_xlabel("x")
    graph3D.set_ylabel("y")
    graph3D.set_zlabel("z")
    
    # Customize each 2D plot
    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(np.min(set_xy), np.max(set_xy)), cmap=cmap), ax=xy, label='Euclidian distance')
    xy.set_xlabel("x")
    xy.set_ylabel("y")

    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(np.min(set_yz), np.max(set_yz)), cmap=cmap), ax=yz, label='Euclidian distance')
    yz.set_xlabel("y")
    yz.set_ylabel("z")

    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(np.min(set_xz), np.max(set_xz)), cmap=cmap), ax=xz, label='Euclidian distance')
    xz.set_xlabel("x")
    xz.set_ylabel("z")   

    # Add title for entire figure
    fig.suptitle("Lorenz Attractor")
    
    # Show input data on figure
    graph3D.set_title("(x, y, z) = (" + str(x[0]) + ", " + str(y[0]) + ", " + str(z[0]) + ")\n" + 
                      "(" +  r"$\sigma$, " + r"$\beta$, "+ r"$\rho$) = (" + str(sigma) + ", " + str(beta) + ", " + str(ro) + ")\n" + 
                      "(dt, N) = " + "(" + str(dt) + ", " + str(N) + ")"
                      "\nElapsed coordinates computation time: " + str(time_elapsed))
    
    # Maximize figure
    

    if file_name is not None:
        plt.savefig(file_name, dpi=240)
    else:
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()
