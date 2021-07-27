import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from colfunc import lorenz

# Set initial conditions
x = [1.]; y = [1.]; z = [1.]
#x = [0]; y = [1]; z = [1.05]
#s = []; t =[]; u =[]

# Generate set of system parameters (timestep, length), (dt, N) 
#dt = 10.0 ** (-1 * np.arange(5))
#N = 5 * 10 ** np.arange(2,7)
dt = 0.001
N = 50000

sigma = [10, 10, 10, 14, 14]
beta = [8/3, 8/3, 8/3, 8/3, 13/3]
ro = [6, 16, 28, 28, 28]

x, y, z = lorenz.euler(x, y, z, sigma[0], ro[0], beta[0], dt, N)
# xarray = np.zeros([N, 5])
# yarray = np.zeros([N, 5])
# zarray = np.zeros([N, 5])


# for i in np.arange(len(sigma)):
#     s, t, u = lorenz.euler(x, y, z, sigma[i], ro[i], beta[i], dt, N)


    
fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot(x, y, z, lw = 0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Lorenz Attractor")

plt.subplot(131)
plt.plot(x,y)
plt.subplot(132)
plt.plot(y,z)
plt.subplot(133)
plt.plot(x,z)

