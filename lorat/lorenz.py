import numpy as np
import timeit

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
    time_start = timeit.default_timer()
    for i in np.arange(0, N-1):

        x.append(x[i] + dt * sigma * (y[i] - x[i]))
        y.append(y[i] + dt * x[i] * (ro - z[i]) - dt * y[i])
        z.append(z[i] + dt * x[i] * y[i] - dt * betta * z[i])
        
    time_elapsed = timeit.default_timer()-time_start
    return [x, y, z, time_elapsed]
