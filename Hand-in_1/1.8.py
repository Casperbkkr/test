from Stoch import Stoch
import numpy as np
from matplotlib import pyplot as plt

# define drift constant
mu = 0.4
# define volatility
sigma = 0.05
# define dt
dt = 10E-2
# define S(0) for paths
S0 = 0.7
# define time to be simulated in years
T = 3
# calculate number of steps to be taken
n_steps = int(T/dt)

# model the stock paths
GBM = Stoch(dt, mu, sigma, n_steps, n_paths=10, years=T, S0=S0)
stock_paths = GBM.GBM_paths

# a) show stock paths
GBM.show_paths()

# b) calculate the running sum of square increments

# calculate different between s(t) and s(t+1) for all t
dSt = np.diff(stock_paths, axis=0)
# calculate square of all delta s(t)
dSt_sq = np.square(dSt)
# take sum
RSSI = dSt_sq.cumsum(axis=0)

plt.plot(RSSI)
plt.show()


# c)
