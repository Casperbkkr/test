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

# calculate var(W(t)), (t/T)var(T-t), cov(W(t),(t/T)W(T-t)) for all times t
Var_Wt = np.var(Wt, axis=0)
Var_tWT_min_t = np.var(t_div_T_WT_min_t, axis=0)
Cov_Wt = 1

# calculate the analytically found identity for the variance.

# plot results
plt.plot(time, Var_Xt)
plt.show()