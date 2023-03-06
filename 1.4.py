from Stoch import Stoch
import numpy as np

dt = 0.001
T = 10
n_steps = int(10/dt)
Wt = Stoch(dt, 1, 1, n_steps).Wiener_paths

t_div_T = (np.arange(0, T, dt))/T
Xt = Wt