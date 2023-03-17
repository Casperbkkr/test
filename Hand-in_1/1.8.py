from Stoch import Stoch
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



def calc_RSSI(data) -> pd.DataFrame:

	if type(data) != np.ndarray:
		df_data = data
		df_out = pd.DataFrame()
		for column in df_data.columns:
			dSt = np.diff(df_data[column].values)
			dSt_sq = np.square(dSt)
			RSSI = dSt_sq.cumsum()
			df_out[column] = RSSI
		return df_out

	else:
		dSt = np.diff(data, axis=0)
		dSt_sq = np.square(dSt)
		RSSI = dSt_sq.cumsum()
		return pd.DataFrame(RSSI)


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
#GBM.show_paths()

# b)
# calculate the running sum of square increments

# calculate different between s(t) and s(t+1) for all t
dSt = np.diff(stock_paths, axis=0)
# calculate square of all delta s(t)
dSt_sq = np.square(dSt)
# calculate the cumulative sum
RSSI = dSt_sq.cumsum(axis=0)
RSSI = calc_RSSI(stock_paths)

#plot the RSSI
plt.plot(RSSI)
plt.show()

# c)
# Calculate the RSSI for stocks
df = pd.read_csv("daily_returns.csv", index_col="Date")
df_RSSI = calc_RSSI(df)

# plot the stock data RSSI
plt.plot(df_RSSI.iloc[:, 2].values)
plt.show()
