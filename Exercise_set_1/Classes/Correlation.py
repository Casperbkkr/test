import pandas as pd
import numpy as np



class Correlation:





	def __init__(self, filename: str) -> None:
		# open the daily returns file to use a returns
		self.daily_returns = pd.read_csv(filename)
		# calculate Covariance matrix
		self.Cov = self._Cov(self.daily_returns)
		# calculate Standard deviation of each stock
		self.Sigma = self._Sigma(self.daily_returns)
		# calculate Pearson correlation coefficient matrix
		self.Corr = self._Corr(self.Cov, self.Sigma)
		# get stocks that are minimally correlated from correlation matrix
		self.min_s1, self.min_s2, self.min_stock_names = self._Min_max_correlation(self.Corr,
		                                                                           self.daily_returns,
		                                                                           min,
		                                                                           pd.DataFrame.idxmin)
		# get stocks that are maximally correlated from correlation matrix
		self.max_s1, self.max_s2, self.max_stock_names = self._Min_max_correlation(self.Corr,
		                                                                           self.daily_returns,
		                                                                           max,
		                                                                           pd.DataFrame.idxmax)


	def _Cov(self, returns) -> pd.DataFrame:
		# return the covariance matrix fo all stocks
		return returns.cov()


	def _Sigma(self, returns) -> pd.Series:
		# calculate the variance of all stocks
		var = returns.var()
		#  return square root of variance
		return var.apply(np.sqrt)


	def _Corr(self, cov, sigma) -> pd.DataFrame:
		# calculate the correlation matrix of the stocks
		sigma1_o_sigma2 = np.outer(sigma, sigma)
		# return correlation matrix
		return np.divide(cov, sigma1_o_sigma2)


	def _Min_max_correlation(self, corr, returns, min_max, id_min_max) -> (pd.Series, pd.Series, (str, str)):
		# calculate absolute value of correlation
		corr_abs = corr.abs()

		# get stocks names with of minimum column values
		if id_min_max == pd.DataFrame.idxmax:
			np.fill_diagonal(corr_abs.values, 0)

		locations = id_min_max(corr_abs)

		# define functions to extract minimum correlation coefficient of columns in matrix
		col = lambda j: corr_abs.columns[j]
		row = lambda i: locations[i]
		packer = lambda i: (corr_abs.loc[col(i), row(i)])

		# get minima using above function, also get corresponding stock names
		mini_maxi = [packer(i) for i in range(0, corr.shape[0])]
		stock_names = [(col(i), row(i)) for i in range(0, corr.shape[0])]

		# get minimum of minima and return
		minimum_maximum = min_max(mini_maxi)
		min_max_stocks = stock_names[mini_maxi.index(minimum_maximum)]

		# return the returns of the stocks that are minimally or maximally correlated and also the names
		return returns[min_max_stocks[0]], returns[min_max_stocks[1]], min_max_stocks
