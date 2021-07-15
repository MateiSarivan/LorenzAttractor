import numpy as np

def euler(x, y, z, sigma, ro, betta, dt, N):
    
    """
    

    Returns
    -------
    x : List
        DESCRIPTION.
    y : List
        DESCRIPTION.
    z : List
        DESCRIPTION.

    """
    for i in np.arange(0, N-1):

        x.append(x[i] + dt * sigma * (y[i] - x[i]))
        y.append(y[i] + dt * x[i] * (ro - z[i]) - dt * y[i])
        z.append(z[i] + dt * x[i] * y[i] - dt * betta * z[i])
        
    return x, y, z
