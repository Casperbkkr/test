#!/usr/bin/env python

from Asset import Asset
#import polars as pl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("island-data-bottle-round-2/prices_round_2_day_0.csv", delimiter=";")

df_c = df.loc[df['product'] == "COCONUTS"]
df_c.reset_index(drop=True, inplace=True)
df_c = df_c.rename(columns={"mid_price": "mid_price_c"})
df_p = df.loc[df['product'] == "PINA_COLADAS"]
df_p.reset_index(drop=True, inplace=True)
df_p = df_p.rename(columns={"mid_price": "mid_price_p"})

cov = pd.concat([df_c["mid_price_c"], df_p["mid_price_p"]], axis=1)
a = cov.rolling(200).cov().unstack()['mid_price_p']['mid_price_c']


#plt.plot(a)
#plt.show()


ratio = df_c["mid_price_c"]/df_p["mid_price_p"]
d = 300
x_mean = ratio.rolling(d).mean()
x_std_dev = np.sqrt(ratio.rolling(d).var())

int_upper = x_mean + x_std_dev
int_lower = x_mean - x_std_dev
upper = np.ones(ratio.shape[0])*int_upper
np.roll(upper, 1)
lower = np.ones(ratio.shape[0])*int_lower

np.roll(lower, 1)

print(x_std_dev)
plt.plot(ratio)
plt.plot(upper)
plt.plot(lower)
plt.show()

var = ratio.rolling(400).var()

plt.plot(ratio)
plt.show()

corr = cov.rolling(400).corr().unstack()['mid_price_p']['mid_price_c']

plt.plot(corr)
plt.show()



