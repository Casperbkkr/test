import pandas as pd
import matplotlib.pyplot as plt


# open csv file with daily returns
df = pd.read_csv("daily_returns.csv", index_col="Date")

# a) plot two stocks that are not dependent

# date = df["Date"].tolist()
stock1 = df["CSCO"].tolist()
stock2 = df["TRNS"].tolist()

plt.scatter(stock1, stock2)
plt.show()

# b) plot two stocks that are dependent

stock1 = df["CSCO"].tolist()
stock2 = df["TRNS"].tolist()

plt.scatter(stock1, stock2)
plt.show()

