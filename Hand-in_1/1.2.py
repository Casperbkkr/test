from Stoch import Stoch
import numpy as np

# Parameters
# Drift coefficient
mu = 0.1
# Volatility
sigma = 0.3
# dt
dt = 0.00001


n_steps = int(5/dt)
if n_steps % 5 != 0:  # make sure that steps are correct amount
	n_steps = n_steps+1

# Create paths of wiener process
paths = Stoch(dt, mu, sigma, n_steps, n_paths=10)
Wiener_path = paths.Wiener_paths

# First calculate the right part of the equation

# Calculate increments of Wiener process
dWs = np.diff(Wiener_path)

# Multiply by the 5-tdt
int_dWs = (5 - np.arange(dt, 5+dt, dt)) * dWs

# Sum to finish integrating
S_int_dWs = int_dWs.sum(axis=1)

# Now calculate the left part of the equation
int_ds = np.trapz(Wiener_path, dx=dt)


# Calculate error between integrals of the same path
error = S_int_dWs - int_ds
print(error)
