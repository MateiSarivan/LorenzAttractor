def graph3D(x, y, z):
    
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.plot(x, y, z, lw = 0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Lorenz Attractor")

    return

def graph2D(x, y, z):

    plt.subplot(131)
    plt.plot(x,y)
    plt.subplot(132)
    plt.plot(y,z)
    plt.subplot(133)
    plt.plot(x,z)

    return