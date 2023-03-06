import numpy as np
import matplotlib.pyplot as plt

class Stoch:
	def __init__(self, dt, mu, sigma, n_steps, *, years=1, n_paths=1, seed=None, S0=100):
		self.dt = dt
		self.mu = mu
		self.sigma = sigma
		self.n_steps = n_steps
		self.n_paths = n_paths
		self.seed = seed
		self.S0 = S0
		self.years = years
		self.Random_walk_paths = self._Random_walk(dt, n_steps, n_paths=n_paths, seed=seed)
		self.GBM_paths = self._GBM(dt, mu, sigma, n_paths=n_paths, seed=seed, S0=S0)
		self.Wiener_paths = self._Wiener(n_paths)

	def _Random_walk(self, dt, n_steps, *, n_paths=1, seed=None):
		if seed is not None:
			np.random.seed(seed)
		return np.random.normal(0.0, np.sqrt(dt), [n_paths, n_steps])

	def _Wiener(self, n_paths):
		zeros = np.zeros((n_paths, 1))
		return np.concatenate((zeros, self.Random_walk_paths.cumsum(axis=1)), axis=1)

	def _GBM(self, dt, mu, sigma, *, n_paths=1, seed=None, S0=100):
		St = (mu - sigma ** 2 / 2) * dt + sigma * self.Random_walk_paths
		expSt = (np.exp(St)).T
		expStplus = np.vstack([np.ones(n_paths), expSt])
		gbm_paths = S0 * expStplus.cumprod(axis=0)
		return gbm_paths

	def show_paths(self):

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


