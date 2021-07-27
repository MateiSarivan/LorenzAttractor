import numpy as np
import timeit

def euler(x, y, z, sigma, beta, ro, dt, N):
    
    """
    Finds the coordinates (x, y, z) for the Lorenz attractor by solving a system of three equations dependent on
    sigma, beta, ro and time using the finite-difference method (Euler). 
         
        x[n+1] = x[n] + dt * sigma * (y[n] - x[n])

        y[n+1] = y[n] + dt * x[n] * (ro - z[n]) - dt * y[n]

        z[n+1] = z[n] + dt * x[n] * y[n] - dt * beta * z[n]
        
        where n belongs {0, 1, ..., N}, and dt is the time step.
    
    Note: as N increases dt should decrease to maintain the same observation interval.

    Parameters
    -------
    
    Initial conditions

    x : List of float
        Initial value of x.
    y : List of float
        Initial value of y.
    z : List of float
        Initial value of z.
    
    Model parameters

    sigma: Float, optional
        Value of sigma. Example values: 10, or 14.    
    beta: Float, optional
        Value of beta. Example values: 8/3 or 13/3.
    ro: Float, optional
        Value of ro. Example values: 6, 16, or 28.

    dt: Float, optional
        Iteration step. Example value: 0.01.
    N: Float, optional
        Length of iteration. Example value: 50000.

    Returns
    -------
    x : List of float
        A list containing all values of x from the initial condition to N.
    y : List floats
        A list containing all values of y from the initial condition to N.
    z : List of float
        A list containing all values of z from the initial condition to N.

    Example
    -------
    >>> euler(x=[1], y=[1], z=[1], sigma=10, beta=8/3, ro=28, dt=0.01, N=3)
    ([1, 1.0, 1.026], [1, 1.26, 1.518], [1, 0.983, 0.969])
    
    """
    
    time_start = timeit.default_timer()
    for i in np.arange(0, N-1):

        x.append(round(x[i] + dt * sigma * (y[i] - x[i]),3))
        y.append(round(y[i] + dt * x[i] * (ro - z[i]) - dt * y[i], 3))
        z.append(round(z[i] + dt * x[i] * y[i] - dt * beta * z[i], 3))
        
    time_elapsed = timeit.default_timer()-time_start
    return x, y, z

if __name__== '__main__':
    import doctest
    doctest.testmod(verbose = True)