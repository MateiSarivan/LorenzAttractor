from lorat.lorenz import euler

def test_euler():
    assert euler(x=[1], y=[1], z=[1], sigma=10, beta=8/3, rho=28, dt=0.01, N=3) == ([1, 1.0, 1.026], [1, 1.26, 1.518], [1, 0.983, 0.969])