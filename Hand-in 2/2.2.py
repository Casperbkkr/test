#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from Classes.GBM import GBM


# define dt
dt = 0.001
# define upper bound T
T = 15
# calculate number of timesteps
n_steps = int(T / dt)
# define the number of paths to simulate
n_paths = 10000

# model Wiener process
Wt = GBM(dt, 1, 1, n_steps, n_paths=n_paths).Wiener_paths

# create time array
time = np.arange(0, T + dt, dt)

# calculate t/T for all t
t_div_T = time / (3*T)

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
c = 3
Var_analytic = time + (np.square(time) / (c**2 * (T ** 2))) * (T - time) - 2 * (time / (c*T)) * Cov_Wt # TODO check if this is correct

# calculate absolute error
error = abs(Var_analytic - Var_Xt)

# calculate confidence intervals
upper1 = np.sqrt(Var_analytic)
lower1 = (-1)*upper1

upper2 = 2* upper1
lower2 = 2* lower1

#plot the results
plt.style.use("seaborn")
fig, axs = plt.subplots(ncols=2, nrows=2)
fig.suptitle(("$X(t) = W(t)- \dfrac{t}{30}W(15-t)$ \n $dt = $" + str(dt)))

gs = axs[1, 1].get_gridspec()
# remove the underlying axes
for ax in axs[0:, -1]:
    ax.remove()
axbig = fig.add_subplot(gs[0:, -1])

axs[0,0].plot(time, Var_analytic, label="Analytic")
axs[0,0].plot(time, Var_Xt, label="Numerical")
axs[0,0].title.set_text("Var(X(t)) vs time")
axs[0,0].legend()
axs[0,0].set_ylabel("Var$(X(t))$")
axs[0,0].set_xlabel("Time")

axs[1,0].plot(time, error, label=error)
axs[1,0].title.set_text("Absolute error vs time")
axs[1,0].set_ylabel("Absolute Error")
axs[1,0].set_xlabel("Time")

# Require numpy array that is the same shape as St
n_show = 10 # TODO Do we need the plume?
tt = np.full(shape=(n_show, n_steps + 1), fill_value=time).T
axbig.plot(tt, Wt[:n_show,:].T)
axbig.fill_between(
    time, upper2, lower2, color='r', alpha=.15)
axbig.fill_between(
    time, upper1, lower1, color='b', alpha=.15)
axbig.set_ylabel("X(t)")
axbig.set_xlabel("Time")
axbig.title.set_text("Sample paths of X(t)")
fig.tight_layout()

plt.show()


