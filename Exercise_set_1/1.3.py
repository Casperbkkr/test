#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from math import exp

from Classes.Stoch import Stoch

# number of years to model
years = 7

# number of steps to be taken to simulate those years and the corresponding step size
n_steps = 10000
dt = years / n_steps

# number of paths to simulate
n_paths = 1000

# defining drift an volatility for X(t) and X0
mu1 = 0.04
sigma1 = 0.38
X0 = 2.1

# make paths for X(t)
Xt = Stoch(dt, mu1, sigma1, n_steps, years=years, S0=X0, n_paths=n_paths)
X_GBM_paths = Xt.GBM_paths

# defining drift an volatility for Y(t) and Y0
mu2 = 0.1
sigma2 = 0.15
Y0 = 0.7

# make paths for Y(t)
Yt = Stoch(dt, mu2, sigma2, n_steps, years=years, S0=Y0, n_paths=n_paths)
Y_GBM_paths = Yt.GBM_paths

# calculate the difference between both paths and divide by half.
Xt_min_Yt = np.vstack((0.5 * (X_GBM_paths[-1] - Y_GBM_paths[-1]) for i in range(0, 101)))

# make array of all strike prices
strikes = np.arange(0, 10.1, 0.1)
# turn into matrix with strike prices stacked as rows
strikes_matrix = np.vstack((strikes for i in range(n_paths))).T

# calculate maximum of difference in paths compared to strike price
max_strike_paths = np.maximum(Xt_min_Yt, strikes_matrix)

# calculate mean for each path
expectation = np.mean(max_strike_paths, axis=1)

# divide by savings account at t=T
MT = exp(0.06 * 7)
Mt_inv = 1 / (MT * np.ones(strikes.shape[0]))

# calculate the expectation
expectation_div_Mt = Mt_inv * expectation

# plot the value
plt.style.use('seaborn')
plt.plot(strikes, expectation_div_Mt)
plt.xlabel("K")
plt.ylabel("V(t)")
plt.show()
