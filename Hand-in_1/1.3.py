from Stoch import Stoch
import numpy as np
import matplotlib.pyplot as plt
from math import exp


# number of years to model
years = 7
# number of steps to be taken to simulate those years
n_steps = 10000
dt = years / n_steps
n_paths = 100
# defining drift an volatility for X(t) and X0
mu1 = 0.04
sigma1 = 0.38
X0 = 0.21
# make paths for Y(t)
Xt = Stoch(dt, mu1, sigma1, n_steps, years=1, S0=X0, n_paths=n_paths)
X_GBM_paths = Xt.GBM_paths

# defining drift an volatility for Y(t) and Y0
mu2 = 0.1
sigma2 = 0.15
Y0 = 0.7
# make paths for X(t)
Yt = Stoch(dt, mu2, sigma2, n_steps, years=years, S0=Y0, n_paths=n_paths)
Y_GBM_paths = Yt.GBM_paths


# calculate the difference between both paths and divide by half.
Xt_min_Yt = (np.vstack([0.5 * (X_GBM_paths[-1] - Y_GBM_paths[-1]) for i in range(n_paths + 1)]))
# make array of all strike prices
strikes = np.arange(0, 10.1, 0.1)
# calculate maximum of difference in paths compared to strike price
max_strike_paths = np.array([np.maximum(Xt_min_Yt[:, i], strikes) for i in range(n_paths)])
# calculate mean for each path
expectation = np.mean(max_strike_paths, axis=0)
# divide by savings account
MT = exp(1.06)**7
Mt_inv = 0.1 * (MT * np.ones(strikes.shape[0]))
expectation_div_Mt = Mt_inv * expectation


plt.scatter(strikes, expectation)
plt.show()

Yt.show_paths()
Xt.show_paths()
