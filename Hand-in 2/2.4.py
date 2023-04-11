import numpy as np
import itertools
import pandas as pd
import matplotlib.pyplot as plt

from math import exp

from Classes.GBM import GBM

# parameters
T = 1
n_steps = 1000
dt = T/n_steps
n_paths = 100000
sigma1 = 0.4 # TODO check if sigma's uncorrelated
sigma2 = 0.15
r = 0.01
X0 = 1
Y0 = 1

def Two_asset_option(S1: np.array, S2: np.array) -> float:
	S1_T = S1[-1, :]
	S2_T = S2[-1, :]
	max_T = np.maximum(S1_T, S2_T)
	value = np.mean(max_T)
	return value

def Sigma_cholesky(rho: float, sig1: float, sig2: float) -> float:
	sigma2_cor = rho*sig1 + np.sqrt(1 - rho**2) *sig2
	return sigma2_cor

# make correlated paths of gbm for rho=0.9
rho = 0.9
sigma2_cor = Sigma_cholesky(rho, sigma1, sigma2)
Xt_max = GBM(dt, r, sigma1, n_steps, years=T, n_paths=n_paths, S0=X0).GBM_paths
Yt_max = GBM(dt, r, sigma2_cor, n_steps, years=T, n_paths=n_paths, S0=Y0).GBM_paths

value_max = Two_asset_option(Xt_max, Yt_max)


# make correlated paths of gbm for rho=0.9
rho = -0.9
sigma1_cor = Sigma_cholesky(rho, sigma1, sigma2)
Xt_min = GBM(dt, r, sigma1, n_steps, years=T, n_paths=n_paths, S0=X0).GBM_paths
Yt_min = GBM(dt, r, sigma1_cor, n_steps, years=T, n_paths=n_paths, S0=Y0).GBM_paths

value_min = Two_asset_option(Xt_min, Yt_min)

print(value_max, value_min)


x=1

