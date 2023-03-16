from Stoch import Stoch
import numpy as np
import matplotlib.pyplot as plt

# define dt
dt = 0.001
# define upper bound T
T = 10
# calculate number of timesteps
n_steps = int(T/dt)
# model Wiener process
Wt = Stoch(dt, 1, 1, n_steps, n_paths=10000).Wiener_paths

# create time array
time = np.arange(0, T+dt, dt)
# calculate t/T for all t
t_div_T = time/T
# reverse the Wiener process to obtain W(10-t)
WT_min_t = np.flip(Wt, 1)
# multiply by t/T
t_div_T_WT_min_t = t_div_T * WT_min_t
# calculate X(t)
Xt = Wt - (t_div_T * WT_min_t)


# calculate the variance of X(t) for all times t as defined in the exercise
Var_Xt = np.var(Xt, axis=0)

# calculate the analytically found identity for the variance
Cov_Wt = np.fmin(time, 10-time)
cov_analytic = time + (np.square(time)/100)*(T-time) - (time/5)*Cov_Wt


# calculate error
error = abs(cov_analytic - Var_Xt)


fig, axs = plt.subplots(2)
fig.suptitle('Absolute error vs time')
axs[0].plot(time, cov_analytic)
axs[0].plot(time, Var_Xt)
axs[1].plot(time, error)
plt.show()