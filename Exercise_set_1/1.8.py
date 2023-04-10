#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Classes.Stoch import Stoch
from Classes.Correlation import Correlation



def calc_RSSI(df_data: pd.DataFrame) -> pd.DataFrame:
	df_out = pd.DataFrame()
	for column in df_data.columns:
		dSt = np.diff(df_data[column].values)
		dSt_sq = np.square(dSt)
		RSSI = dSt_sq.cumsum()
		df_out[column] = RSSI
	return df_out


# define drift constant
mu = 0.05
# define volatility
sigma = 0.5
# define dt
dt = 10 ** (-2)
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
stock_paths: np.array = GBM.GBM_paths[:-1, :]

# b)
# calculate the running sum of square increments
RSSI = GBM.RSSI  # TODO get this out of class

# Define time interval correctly
time = np.linspace(0, 3, n_steps)
tt = np.full(shape=(n_paths, n_steps), fill_value=time).T

# Plot results
plt.style.use('seaborn')
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True)

ax1.set_title("Asset paths")
ax1.set_xlabel("Years $(t)$")
ax1.set_ylabel("$S(t)$")
ax1.plot(tt, stock_paths)

ax2.set_title("Rolling sum of square increments")
ax2.set_xlabel("Years $(t)$")
ax2.set_ylabel("RSSI")
ax2.plot(tt, RSSI)

fig.suptitle(
	"$dS_t = \mu S_t dt + \sigma S_t dW_t$\n $S_0 = {0}, \mu = {1}, \sigma = {2}$".format(S0,
	                                                                                      mu,
	                                                                                      sigma))
fig.show()
# Require numpy array that is the same shape as St


# c)
# get the daily returns of maximally and minimally correlated stocks from exercise 7.
C1 = Correlation("Data/daily_returns.csv")
Date = pd.read_csv("Data/daily_returns.csv")["Date"]

# get stock names
n1, n2 = C1.min_stock_names
n3, n4 = C1.max_stock_names

# make new dataframe with the max-min corr stocks combined.
s1 = C1.min_s1.to_numpy()
s2 = C1.min_s2.to_numpy()
s3 = C1.max_s1.to_numpy()
s4 = C1.max_s2.to_numpy()

m = (np.vstack([s1, s2, s3, s4])).T
df = pd.DataFrame(data=m, columns=[n1, n2, n3, n4])
df.set_index(Date, inplace=True)

# Calculate the RSSI for stocks
df_RSSI = calc_RSSI(df)

Date.drop(Date.tail(1).index, inplace=True)
df_RSSI.set_index(Date, inplace=True)

df.drop(df.tail(1).index, inplace=True)
df_out = pd.concat([df, df_RSSI], axis=1)
# Reorder the columns
df_out = df_out.iloc[:, [0, 4, 1, 5, 2, 6, 3, 7]]

fig = df_out.plot(subplots=True,
                  layout=(4, 2),
                  color=['r', 'r', 'g', 'g', 'b', 'b', 'k', 'k'],
                  )
[fig[:, 0][i].set_ylabel("Daily returns") for i in range(0, 4)]

[fig[:, 1][i].set_ylabel("RSSI") for i in range(0, 4)]
fig[0, 0].sharey(fig[1, 0])
fig[2, 0].sharey(fig[3, 0])

fig[0, 1].sharey(fig[1, 1])
fig[3, 1].sharey(fig[2, 1])

fig[0, 0].set_title("Asset return path")
fig[0, 1].set_title("Rolling sum of square increments")

plt.show()


x = 1
