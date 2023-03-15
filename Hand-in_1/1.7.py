import pandas as pd
import matplotlib.pyplot as plt


def calc_daily_returns(df_data):
	new_col = df_data['Close'] - df_data['Open']
	return new_col


def calc_RSSI(df_data):
	df_data
	return


df = pd.read_csv("daily_returns.csv")
df = df.sort_values(by=["Date"])
df.reset_index(inplace=True)
df.drop(columns=["index"], inplace=True)

date = df["Date"].tolist()
stock1 = df["CSCO"].tolist()
stock2 = df["TRNS"].tolist()

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(date[0:600], stock1[0:600], s=1, c='b', marker="s", label='first')
ax1.scatter(date[0:600], stock2[0:600], s=1, c='r', marker="o", label='second')
plt.legend(loc='upper left')
plt.show()

