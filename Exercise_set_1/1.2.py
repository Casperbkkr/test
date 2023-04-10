#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from Classes.Stoch import Stoch



def Int_error(ds: float, n_paths: np.array) -> int:
	# Calculate error between the different integrals

	# Calculate the number of steps to take
	n_steps = int(5 * (1 / ds))

	# Create paths of Wiener process
	paths = Stoch(ds, 1, 1, n_steps, n_paths=n_paths)
	Wiener_path = paths.Wiener_paths

	# First calculate the right part of the equation
	# Calculate increments of Wiener process
	dWs = np.diff(Wiener_path)

	# Multiply by the 5-s
	S = np.linspace(ds, 5, n_steps)
	C = 5 - S  # calculate before multiplying by Dws
	int_dWs = C * dWs

	# Sum to finish integrating
	# S_int_dWs = ne.evaluate('sum(int_dWs, axis=1)')
	S_int_dWs = np.sum(int_dWs, axis=1)
	# Now calculate the left part of the equation
	int_ds = np.trapz(Wiener_path, dx=ds)

	# Calculate error between integrals of the same path
	error = np.abs(S_int_dWs - int_ds)

	# return average error
	return np.mean(error)

# specify size of steps between different ds
ds_step_size = 0.001
Ds = np.arange(ds_step_size, 1, ds_step_size)

Results = [Int_error(ds, 1000) for ds in Ds]

plt.style.use('seaborn')
plt.plot(Ds, Results)
plt.xlabel("ds")

plt.ylabel("Mean absolute error")
plt.show()
