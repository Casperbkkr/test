#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from Classes.Stoch import Stoch



# define dt
dt = 0.0001
# define upper bound T
T = 10
# calculate number of timesteps
n_steps = int(T / dt)
# define the number of paths to simulate
n_paths = 1000

# model Wiener process
Wt = Stoch(dt, 1, 1, n_steps, n_paths=n_paths).Wiener_paths

# create time array
time = np.arange(0, T + dt, dt)

# calculate t/T for all t
t_div_T = time / T

# reverse the Wiener process to obtain W(10-t)
WT_min_t = np.flip(Wt, axis=1)

# multiply by t/T
t_div_T_WT_min_t = t_div_T * WT_min_t

# calculate X(t)
Xt = Wt - (t_div_T * WT_min_t)

# calculate the variance of X(t) for all times t as defined in the exercise
Var_Xt = np.var(Xt, axis=0)

# calculate the analytically found identity for the variance
Cov_Wt = np.fmin(time, T - time)
cov_analytic = time + (np.square(time) / T ** 2) * (T - time) - 2 * (time / T) * Cov_Wt

# calculate absolute error
error = abs(cov_analytic - Var_Xt)

# plot Var(X(t)) and the absolute error.
plt.style.use("seaborn")
fig, axs = plt.subplots(2)
fig.suptitle(("$X(t) = W(t)- \dfrac{t}{10}W(10-t)$ \n $dt = $" + str(dt)))
axs[0].plot(time, cov_analytic, label="Analytic")

axs[0].plot(time, Var_Xt, label="Numerical")
axs[0].legend()
axs[0].set_ylabel("Var$(X(t))$")

axs[1].plot(time, error)
axs[1].set_ylabel("Absolute Error")
axs[1].set_xlabel("Time")
plt.show()
