from Stoch import Stoch
import numpy as np
# Parameters
# drift coefficent
mu = 0.1
# volatility
sigma = 0.3
dt = 0.001

n_steps = int(5/dt)

# Create paths of wiener process
paths = Stoch(dt, mu, sigma, n_steps, n_paths=1)
Wiener_path = paths.Wiener_paths

# Calculate increments of Wiener process
dWs = np.diff(Wiener_path)

# Multiply by the 5-tdt
int_dWs = (5 - np.arange(dt, 5, dt)) * dWs

# Sum to finish integrating
S_int_dWs = int_dWs.sum(axis=1)

