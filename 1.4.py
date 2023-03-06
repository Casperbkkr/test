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
Wt = Stoch(dt, 1, 1, n_steps).Wiener_paths

# create time array
time = np.arange(0, T+dt, dt)
# calculate t/T for all t
t_div_T = time/T
# reverse the Wiener process to obtain W(10-t)
WT_min_t = np.flip(Wt, 1)
# calculate X(t)
Xt = Wt - (t_div_T * WT_min_t)

# plot results
plt.plot(time, Xt[0])
plt.show()