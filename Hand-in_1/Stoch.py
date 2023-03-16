import numpy as np
import matplotlib.pyplot as plt

class Stoch:
	def __init__(self, dt: float,
	                   mu: float,
	                   sigma: float,
	                   n_steps: int,
	                   *, years: int = 1,
	                   n_paths: int = 1,
	                   seed=None,
	                   S0: float = 100):
		self.dt = dt
		self.mu = mu
		self.sigma = sigma
		self.n_steps = n_steps
		self.n_paths = n_paths
		self.seed = seed
		self.S0 = S0
		self.years = years
		self.Random_walk_paths = self._Random_walk(self.dt, n_steps, n_paths=self.n_paths, seed=seed)
		self.GBM_paths = self._GBM(self.dt, self.mu, self.sigma, n_paths=self.n_paths, seed=seed, S0=S0)
		self.Wiener_paths = self._Wiener(self.n_paths)

	def _Random_walk(self, dt: float, n_steps: int, *, n_paths: int = 1, seed=None) -> np.array:

		if seed is not None: # set seed for numpy if seed is given
			np.random.seed(seed)
		return np.random.normal(0.0, np.sqrt(dt), [n_paths, n_steps])  # returns numpy array with random samples from N(0,sqrt(dt))

	def _Wiener(self, n_paths: int) -> np.array:
		zeros = np.zeros((n_paths, 1))  # add zero as X0
		return np.concatenate((zeros, self.Random_walk_paths.cumsum(axis=1)), axis=1)  # return array with cumulative sum of random walk

	def _GBM(self, dt: int, mu: float, sigma: float, *, n_paths: int = 1, seed=None, S0: float = 100) -> np.array:
		# calculate brownian motion
		St = (mu - ((sigma**2) / 2))*dt + sigma*self.Random_walk_paths
		# take exponent of S(t) and transpose array
		expSt = (np.exp(St)).T
		# start gbm at one
		expStplus = np.vstack([np.ones(n_paths), expSt])
		# multiply by S(0) and take the cumulative product
		gbm_paths = S0 * expStplus.cumprod(axis=0)
		return gbm_paths  # return array with geometric brownian motion paths



	def show_paths(self) -> None:

		# Define time interval correctly
		time = np.linspace(0, self.years, self.n_steps+1)
		# Require numpy array that is the same shape as St
		tt = np.full(shape=(self.n_paths, self.n_steps+1), fill_value=time).T

		plt.plot(tt, self.GBM_paths)
		plt.xlabel("Years $(t)$")
		plt.ylabel("Stock Price $(S_t)$")
		plt.title(
		"$dS_t = \mu S_t dt + \sigma S_t dW_t$\n $S_0 = {0}, \mu = {1}, \sigma = {2}$".format(self.S0, self.mu, self.sigma)
		)
		plt.show()


