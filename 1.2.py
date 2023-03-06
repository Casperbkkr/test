from Stoch import Stoch

# Parameters
# drift coefficent
mu = 0.1
# number of steps
n_steps = 100
# time in years
years = 1
# number of sims
n_paths = 100
# initial stock price
S0 = 100
# volatility
sigma = 0.3
dt=years/n_steps


def dWs(upper, dt, *, path=None):
	if path is None:
		path = Wiener(upper/dt, dt)
	else:
		pass
	return sum((upper - np.arange(dt, upper+dt, dt)) * np.diff(path))
