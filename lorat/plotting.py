import matplotlib.pyplot as plt

def graph(x, y, z, dt, N):
    print("x_0: ", x[0], "    y_0:  ", y[0], "    z_0:   ", z[0])
    print("x_f: ", x[len(x)-1], "    y_f:  ", y[len(x)-1], "    z_f:   ", z[len(x)-1])

    fig = plt.figure(figsize = (6, 6))
    gs = fig.add_gridspec(ncols=7, nrows=3, wspace=1, hspace = 0.5)
    
    graph3D = fig.add_subplot(gs[0:, :3], projection='3d')
    xy = fig.add_subplot(gs[0, 4:])
    yz = fig.add_subplot(gs[1, 4:])
    xz = fig.add_subplot(gs[2, 4:])
    
    
    #fig, ((ax1, ax2), (ax3, ax4, ax5)) = plt.subplots(2, 3)
    
   # graph3D.plot(x, y, z, lw = 0.5)

    s=10
    cmap = plt.cm.viridis
    for i in range(0,N-s,s):
        graph3D.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=cmap(i/N), alpha=0.4)
        xy.plot(x[i:i+s+1], y[i:i+s+1], color=cmap(i/N), alpha=0.4)
        yz.plot(y[i:i+s+1], z[i:i+s+1], color=cmap(i/N), alpha=0.4)
        xz.plot(x[i:i+s+1], z[i:i+s+1], color=cmap(i/N), alpha=0.4)

    graph3D.set_xlabel("x")
    graph3D.set_ylabel("y")
    graph3D.set_zlabel("z")
    graph3D.set_title("Lorenz Attractor")
    
    xy.set_xlabel("x")
    xy.set_ylabel("y")

    yz.set_xlabel("y")
    yz.set_ylabel("z")

    xz.set_xlabel("x")
    xz.set_ylabel("z")   