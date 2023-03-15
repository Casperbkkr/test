
import pandas as pd
from pathlib import Path


sheet = pd.read_csv('daily_returns.csv')

folder = "/Users/casperbakker/Documents/PycharmProjects/Modelling_biosystems/Computational_Finance/stock_market_data" \
         "/nasdaq/csv"

df_output = pd.DataFrame()  # make empty output Dataframe
i = 0


for file in Path(folder).glob('*.csv'): # loop through all files in data
	stock_csv = str(file).split("/")[-1]  # get last part of file path
	stock_name = stock_csv.split(".")[0]  # get stock name without .csv extension
	print(i)
	df_stock = pd.read_csv(file)
	df_stock.set_index('Date', inplace=True)
	df_daily_returns = pd.DataFrame()
	df_daily_returns[stock_name] = calc_daily_returns(df_stock)
	df_output =  pd.concat([df_output, df_daily_returns], axis=1)
	if i == 1000:
		df_output.to_csv("daily_returns.csv")
		break

