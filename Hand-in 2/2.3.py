import numpy as np
import itertools
import matplotlib.pyplot as plt
from math import exp

import pandas as pd

from Classes.GBM import GBM
from Classes.Milstein import Milstein


def value(paths:np.array, K: float) -> float:
	final_price = paths[-1, :]
	strike = K*np.ones(final_price.shape)
	maxi = np.maximum(final_price, strike)
	price = np.mean(maxi)
	discount = exp(-r*T)
	return price*discount

# parameters
T = 4
S0 = 1
r = 0.05
K = 1.6

# function to make sigma(t) for all t
sigma_t = lambda n_steps:  0.6 - 0.2 * np.exp(-1.5 * np.linspace(0, T, n_steps))

# make cartesian product of steps and paths
n = [1000, 10000, 100000]
m = [50, 100, 200, 400]
n_times_m = list(itertools.product(n, m))

# make empty dataframes for results
df_GBM = pd.DataFrame(index=m, columns=n)
df_Milstein = pd.DataFrame(index=m, columns=n)

# simulate Milstein and Euler for all combinations of n_paths and n_steps
for ij in n_times_m:
	n_paths = ij[0]
	n_steps = ij[1]
	sigma = sigma_t(n_steps)
	dt = T/n_steps
	GBM_paths = GBM(dt, r, sigma, n_steps=n_steps, years=T, n_paths=n_paths, S0=S0).GBM_paths
	Milstein_paths = Milstein(dt, r, sigma, n_steps, years=T, n_paths=n_paths, S0=S0).Milstein_paths

	# save the estimated value to the dataframe
	df_GBM.loc[n_steps, n_paths] = value(GBM_paths, K)
	df_Milstein.loc[n_steps, n_paths] = value(Milstein_paths, K)

# write csv's with results
df_GBM.to_csv("GBM_value.csv")
df_Milstein.to_csv("Milstein_value.csv")






x=1

