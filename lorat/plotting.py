import matplotlib.pyplot as plt

def graph3D(x, y, z):
    print("x_0: ", x[0], "    y_0:  ", y[0], "    z_0:   ", z[0])
    print("x_f: ", x[len(x)-1], "    y_f:  ", y[len(x)-1], "    z_f:   ", z[len(x)-1])
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.plot(x, y, z, lw = 0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Lorenz Attractor")

    

def graph2D(x, y, z):

    plt.subplot(131)
    plt.plot(x,y)
    plt.subplot(132)
    plt.plot(y,z)
    plt.subplot(133)
    plt.plot(x,z)

    return