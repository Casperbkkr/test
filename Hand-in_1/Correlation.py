import pandas as pd
import numpy as np




class Correlation:





	def __init__(self, filename):
		# open the daily returns file to use a returns
		self.daily_returns = pd.read_csv(filename)
		# calculate Covariance matrix
		self.Cov = self._Cov(self.daily_returns)
		# calculate Standard deviation of each stock
		self.Sigma = self._Sigma(self.daily_returns)
		# calculate Pearson correlation coefficient matrix
		self.Corr = self._Corr(self.Cov, self.Sigma)
		# get stocks that are minimally correlated from correlation matrix
		self.min_s1, self.min_s2, self.min_stock_names = self._Minimum_correlation(self.Corr, self.daily_returns)
		# get stocks that are maximally correlated from correlation matrix
		self.max_s1, self.max_s2, self.max_stock_names = self._Maximum_correlation(self.Corr, self.daily_returns)


	def _Cov(self, returns) -> pd.DataFrame:
		# calculate the covariance matrix fo all stocks
		return returns.cov()


	def _Sigma(self, returns) -> pd.Series:
		# calcualte the variance of all stocks
		var = returns.var()
		return var.apply(np.sqrt)


	def _Corr(self, cov, sigma) -> pd.DataFrame:
		# calculate the correlation matrix of the stocks
		sigma1_o_sigma2 = np.outer(sigma, sigma)
		return np.divide(cov, sigma1_o_sigma2)


	def _Minimum_correlation(self, corr, returns) -> (pd.Series, pd.Series, (str, str)):
		# calculate absolute value of correlation
		corr_abs = corr.abs()

		# get stocks names with of minimum column values
		locations = corr_abs.idxmin()

		# define functions to extract minimum correlation coefficient of columns in matrix
		col = lambda j: corr_abs.columns[j]
		row = lambda i: locations[i]
		packer = lambda i: (corr_abs.loc[col(i), row(i)])

		# get minima using above function, also get corresponding stock names
		minima = [packer(i) for i in range(0, corr.shape[0])]
		stock_names = [(col(i), row(i)) for i in range(0, corr.shape[0])]

		# get minimum of minima and return
		minimum = min(minima)
		min_stocks = stock_names[minima.index(minimum)]
		return returns[min_stocks[0]], returns[min_stocks[1]], min_stocks


	def _Maximum_correlation(self, corr, returns) -> (pd.Series, pd.Series, (str, str)):

		# calculate absolute value of correlation
		corr_abs = corr.abs()

		# set diagonal to 0 to prevent finding diagonal elements as maximally correlated
		np.fill_diagonal(corr_abs.values, 0)

		# get stocks names with of minimum column values
		locations = corr_abs.idxmax()

		# define functions to extract minimum correlation coefficient of columns in matrix
		col = lambda j: corr_abs.columns[j]
		row = lambda i: locations[i]
		packer = lambda i: (corr_abs.loc[col(i), row(i)])

		# get maxima using above function, also get corresponding stock names
		maxima = [packer(i) for i in range(0, corr.shape[0])]
		stock_names = [(col(i), row(i)) for i in range(0, corr.shape[0])]

		# get maximum of maxima and return
		maximum = max(maxima)
		max_stocks = stock_names[maxima.index(maximum)]


		return returns[max_stocks[0]], returns[max_stocks[1]], max_stocks

