import pandas as pd
from pathlib import Path

folder = "/Users/casperbakker/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/stock_market_data/nasdaq/csv"

# make empty output Dataframe
df_output = pd.DataFrame()
df_out2 = pd.DataFrame()
i = 0
# define max files to read and calculate
max_files = 1000
# loop through all files in data
for file in Path(folder).glob('*.csv'):
	i += 1
	# get last part of file path
	stock_csv = str(file).split("/")[-1]
	# get stock name without .csv extension
	stock_name = stock_csv.split(".")[0]
	# read the csv
	df_stock = pd.read_csv(file)

	# shift the close column to calc daily returns
	df_stock['Close_shift'] = df_stock['Close'].shift(1)
	df_stock.at[0, 'Close_shift'] = 0
	# set the index column to Date
	df_stock.set_index('Date', inplace=True)

	# make new DataFrame
	df_daily_returns = pd.DataFrame()
	df_percentage_returns = pd.DataFrame()
	# save  the daily return to the DataFrame
	if stock_name == "TENX":
		a=1

	df_daily_returns[stock_name] = df_stock['Close'] - df_stock['Close_shift']
	df_percentage_returns[stock_name] = df_stock['Close'] / df_stock['Close_shift']
	# add new stock to the output Dataframe
	df_output = pd.concat([df_output, df_daily_returns], axis=1)
	df_out2 = pd.concat([df_out2, df_daily_returns], axis=1)
	# stop reading files if the max to read files has been met
	if i == max_files:
		break



df_output.index = pd.to_datetime(df_output.index)
df = df_output.sort_values(by=["Date"])

df.reset_index(inplace=True)
df = df[~(df['Date'] < '2010-01-01')]

df.drop(columns=["TENX", "TOPS"], inplace=True)
df.dropna(axis='columns', how="any", inplace=True)
df.set_index(["Date"], inplace=True)

# write to csv
df.to_csv("daily_returns.csv")

df_out2.index = pd.to_datetime(df_out2.index)
df = df_out2.sort_values(by=["Date"])

df.drop(columns=["TENX", "TOPS"], inplace=True)
df.reset_index(inplace=True)
df = df[~(df['Date'] < '2010-01-01')]
df.dropna(axis='columns', how="any", inplace=True)
df.set_index(["Date"], inplace=True)

# write to csv
df.to_csv("daily_relative_returns.csv")
