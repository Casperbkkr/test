from Market import Market

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv("island-data-bottle-round-2/prices_round_2_day_0.csv", delimiter=";")

market = Market(df.head(4*10))
for n in range(10, df.shape[0]):
	df_in = df.head(4*n)
	C, L, U, M = market.calculate_interval(df_in, "COCONUTS", "PINA_COLADAS")
	# current_ratio = df_in[]
	if (L < C) and (C < U):
		x = 1
		#print("in interval")
	else:
		if C > M:
			print("buy lower")
		if C < M:
			print("buy upper")
	x = 1


x = 1