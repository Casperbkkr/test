import numpy as np

from Classes.GBM import GBM

class Milstein:

	def __init__(self,
	             dt,
	             mu,
	             sigma,
	             n_steps,
	             *, years=1,
	             n_paths=1,
	             seed=None,
	             S0=1,
	             Wiener_paths=None) -> None:

		if Wiener_paths == None:
			self.Wiener_paths = GBM(dt, mu, sigma, n_steps, years=years, n_paths=n_paths, seed=seed, S0=S0).Wiener_paths
		else:
			self.Wiener_paths = Wiener_paths
		self.Milstein_paths = self._Milstein(dt, mu, sigma, S0, self.Wiener_paths)


	def _Milstein(self, dt, mu, sigma, S0, W):
		dW =  np.diff(W, axis=1)
		paths = self._M_internal(dt, mu, sigma, S0, dW)
		return paths

	def _M_internal(self, dt, mu, sigma, S0, dW):
		a = dW[:,0:]
		S1 = self._Step(dt, mu, sigma[0,], S0, dW[:, 0])
		if dW.shape[1] == 1:
			return S1
		else:
			return np.vstack( [S1, self._M_internal(dt, mu, sigma[1:], S1, dW[:, 1:])])

	def _Step(self, dt, mu, sigma, S0, dW): #TODO check if this is correct
		a = mu * S0 * dt
		b = sigma * S0 * dW
		c = 0.5 * mu * (dW**2 - dt)
		return S0 + a + b + c





