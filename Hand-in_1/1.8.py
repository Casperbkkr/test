from Stoch import Stoch
from Correlation import Correlation
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



def calc_RSSI(df_data) -> pd.DataFrame:
	df_out = pd.DataFrame()
	for column in df_data.columns:
		dSt = np.diff(df_data[column].values)
		dSt_sq = np.square(dSt)
		RSSI = dSt_sq.cumsum()
		df_out[column] = RSSI
	return df_out


# define drift constant
mu = 0.1

# define volatility
sigma = 0.05

# define dt
dt = 10E-2

# define S(0) for paths
S0 = 0.7

# define time to be simulated in years
T = 3

# calculate number of steps to be taken
n_steps = int(T / dt)

# define the number of paths to simulate
n_paths = 10

# a)
# model the stock paths
GBM = Stoch(dt, mu, sigma, n_steps, n_paths=10, years=T, S0=S0)
stock_paths = GBM.GBM_paths
# show stock paths
GBM.show_paths()

# b)
# calculate the running sum of square increments
RSSI = GBM.RSSI

# plot the RSSI
plt.plot(RSSI)
plt.show()

# c)
# get the daily returns of maximally and minimally correlated stocks from exercise 7.
C1 = Correlation("daily_returns.csv")

# get stock names
n1, n2 = C1.min_stock_names
n3, n4 = C1.max_stock_names

# make new dataframew with the max-min corr stocks combined.
s1 = C1.min_s1.to_numpy()
s2 = C1.min_s2.to_numpy()
s3 = C1.max_s1.to_numpy()
s4 = C1.max_s2.to_numpy()
m = (np.vstack([s1, s2, s3, s4])).T
df = pd.DataFrame(data=m, columns=[n1, n2, n3, n4])

# Calculate the RSSI for stocks
df_RSSI = calc_RSSI(df)

# TODO add correct x-axis with time
# plot the stock data RSSI
plt.plot(df_RSSI.iloc[:, 0].values)
plt.plot(df_RSSI.iloc[:, 1].values)
plt.plot(df_RSSI.iloc[:, 2].values)
plt.plot(df_RSSI.iloc[:, 3].values)
plt.show()
