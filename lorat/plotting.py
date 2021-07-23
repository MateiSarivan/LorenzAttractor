import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def graph(x, y, z, dt, N):
    # print("x_0: ", x[0], "    y_0:  ", y[0], "    z_0:   ", z[0])
    # print("x_f: ", x[len(x)-1], "    y_f:  ", y[len(x)-1], "    z_f:   ", z[len(x)-1])

    fig = plt.figure(figsize = (6, 6))
    gs = fig.add_gridspec(ncols=7, nrows=3, wspace=1, hspace = 0.5)
    
    graph3D = fig.add_subplot(gs[0:, :3], projection='3d')
    xy = fig.add_subplot(gs[0, 4:])
    yz = fig.add_subplot(gs[1, 4:])
    xz = fig.add_subplot(gs[2, 4:])
    
    #Determine euclidian distance from one step to the other
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

    print("Euclidian distance is: ", eucled_3D)    

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

    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(np.min(set_3D), np.max(set_3D)), cmap=cmap), ax=graph3D, orientation = 'horizontal')
    graph3D.set_xlabel("x")
    graph3D.set_ylabel("y")
    graph3D.set_zlabel("z")
    graph3D.set_title("Lorenz Attractor")
    
    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(np.min(set_xy), np.max(set_xy)), cmap=cmap), ax=xy)
    xy.set_xlabel("x")
    xy.set_ylabel("y")

    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(np.min(set_yz), np.max(set_yz)), cmap=cmap), ax=yz)
    yz.set_xlabel("y")
    yz.set_ylabel("z")

    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(np.min(set_xz), np.max(set_xz)), cmap=cmap), ax=xz)
    xz.set_xlabel("x")
    xz.set_ylabel("z")   