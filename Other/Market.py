import pandas as pd
import numpy as np

from Asset import Asset



class Market:





	def __init__(self, df):
		self.data = df
		self.assets = self._create_assets(df)



	def calculate_interval(self, new_data, asset1_name, asset2_name, rolling_depth=200):

		self._update_data(new_data)

		ratio = self.assets[asset1_name].data["mid_price"]/self.assets[asset2_name].data["mid_price"]
		x_mean = ratio.rolling(rolling_depth).mean()
		x_std_dev = np.sqrt(ratio.rolling(rolling_depth).var())

		int_upper = x_mean + 2*x_std_dev
		int_lower = x_mean - 2*x_std_dev

		current_ratio = ratio.tail(1).iloc[0]

		return current_ratio,\
		       int_lower.tail(1).iloc[0],\
		       int_upper[int_upper.shape[0]-1],\
		       x_mean[x_mean.shape[0]-1]

	def _update_data(self, new_data):
		self.data = new_data
		self.assets = self._create_assets(new_data)


	def _create_assets(self, df):
		get_df = lambda name: (df.loc[df['product'] == name]).reset_index(drop=True)
		return {i: Asset(i, get_df(i)) for i in df["product"].unique()}

