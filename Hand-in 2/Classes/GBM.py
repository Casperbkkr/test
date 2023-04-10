import numpy as np
import matplotlib.pyplot as plt




class GBM:





	def __init__(self, dt: float,
	             mu: float,
	             sigma: float,
	             n_steps: int,
	             *, years: int = 1,
	             n_paths: int = 1,
	             seed=None,
	             S0: float = 100) -> None:

		self.dt = dt
		self.mu = mu
		self.sigma = sigma
		self.n_steps = n_steps
		self.n_paths = n_paths
		self.seed = seed
		self.S0 = S0
		self.years = years
		self.Random_walk_paths = self._Random_walk(dt, n_steps, n_paths=n_paths, seed=seed)
		self.Wiener_paths = self._Wiener(n_paths)
		self.GBM_paths = self._GBM(dt, mu, sigma, n_paths=n_paths, S0=S0)
		self.RSSI = self._RSSI(self.GBM_paths)


	def _Random_walk(self, dt: float, n_steps: float, *, n_paths: int = 1, seed=None) -> np.array:
		# set seed for numpy if seed is given
		if seed is not None:
			np.random.seed(seed)
		return np.random.normal(0.0, np.sqrt(dt),
		                        [n_paths, n_steps])  # returns numpy array with random samples from N(0,sqrt(dt))


	def _Wiener(self, n_paths: int) -> np.array:
		# make array with zeros to prepend to all paths
		zeros = np.zeros((n_paths, 1))
		# prepend the zeros array to cummulative sum of the random walk to get the Wiener paths
		Wiener_paths = np.concatenate((zeros, self.Random_walk_paths.cumsum(axis=1)), axis=1)

		return Wiener_paths


	def _GBM(self, dt: int, mu: float, sigma: float, *, n_paths: int = 1, S0: float = 100) -> np.array:

		# calculate brownian motion
		paths = self.Random_walk_paths
		C = (mu - ((sigma ** 2) / 2)) * dt  # calculate to remove from loop
		St = C + sigma * paths

		# take exponent of S(t) and transpose array
		expSt = (np.exp(St)).T

		# start gbm at one
		expStplus = np.vstack([np.ones(n_paths), expSt])

		# Get cumulative product of expStplus
		prodexpStplus = expStplus.cumprod(axis=0)

		# multiply by S(0)
		gbm_paths = S0 * prodexpStplus

		# return array with geometric brownian motion paths
		return gbm_paths


	def _RSSI(self, paths: np.array) -> np.array:
		# calculate the increments between consecutive t's
		dSt = np.diff(paths, axis=0)
		# square the increments
		dSt_sq = np.square(dSt)
		# return cumulative (running) sum of square of increments
		return dSt_sq.cumsum(axis=0)


	def show_paths(self) -> None:
		plt.style.use('seaborn')
		# Define time interval correctly
		time = np.linspace(0, self.years, self.n_steps + 1)
		# Require numpy array that is the same shape as St
		tt = np.full(shape=(self.n_paths, self.n_steps + 1), fill_value=time).T

		plt.plot(tt, self.GBM_paths)
		plt.xlabel("Years $(t)$")
		plt.ylabel("Stock Price $(S_t)$")
		plt.title(
			"$dS_t = \mu S_t dt + \sigma S_t dW_t$\n $S_0 = {0}, \mu = {1}, \sigma = {2}$".format(self.S0,
			                                                                                      self.mu,
			                                                                                      self.sigma)
			)
		plt.show()
