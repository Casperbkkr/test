from Stoch import Stoch
import numpy as np

dt = 1


# number of years to model
years = 7
# number of steps to be taken to simulate those years
n_steps = int((7*365)/dt)

# defining drift an volatility for X(t) and X0
mu1 = 0.04
sigma1 = 0.38
X0 = 0.7

Xt = Stoch(dt, 0.2, 0.65, n_steps, years=1, S0=X0)

# defining drift an volatility for Y(t) and Y0
mu2 = 0.1
sigma2 = 0.15
Y0 = 2.1

Yt = Stoch(dt, mu2, sigma2, n_steps, years=years, S0=Y0)

Yt.show_paths()
Xt.show_paths()



