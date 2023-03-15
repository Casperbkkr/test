from Stoch import Stoch
import numpy as np
import matplotlib.pyplot as plt



# number of years to model
years = 1
# number of steps to be taken to simulate those years
n_steps = 10000
dt = years/n_steps

# defining drift an volatility for X(t) and X0
mu1 = 0.04
sigma1 = 0.38
X0 = 0.7
# make paths for Y(t)
Xt = Stoch(dt, mu1, sigma1, n_steps, years=1, S0=X0, n_paths=100)
X_GBM_paths = Xt.GBM_paths


# defining drift an volatility for Y(t) and Y0
mu2 = 0.1
sigma2 = 0.15
Y0 = 2.1
# make paths for X(t)
Yt = Stoch(dt, mu2, sigma2, n_steps, years=years, S0=Y0, n_paths=100)
Y_GBM_paths = Yt.GBM_paths





Yt.show_paths()
Xt.show_paths()



