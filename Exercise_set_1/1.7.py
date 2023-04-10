#!/usr/bin/env python3
import matplotlib.pyplot as plt

from Classes.Correlation import Correlation


# use Correlation class to find maximally and minimally correlated stocks
C1 = Correlation("Data/daily_relative_returns.csv")


# a) plot two stocks that are not dependent
stock1 = C1.min_s1.tolist()
stock2 = C1.min_s2.tolist()
names_min = C1.min_stock_names


# make scatter plot of minimally dependent stocks
plt.style.use('seaborn')
plt.scatter(stock1, stock2, s=20)

plt.title("Daily returns from 2010 to present \n"
          "'Mid Penn Bancorp Inc' vs 'Cinedigm'")

plt.ylim(-8, 8)
plt.xlim(-8, 8)

plt.xlabel(names_min[0])
plt.ylabel(names_min[1])
plt.show()


# b) plot two stocks that are dependent
stock1 = C1.max_s1.tolist()
stock2 = C1.max_s2.tolist()
names_max = C1.max_stock_names

# make scatter plot of maximally dependent stocks
plt.scatter(stock1, stock2, s=20)
plt.title("Daily returns from 2010 to present \n"
          "'Calamos Conv. Opptys. & Income fund' vs 'Calamos Conv. & Hi Income fund'")

plt.ylim(-2, 2)
plt.xlim(-2, 2)

plt.xlabel(names_max[0])
plt.ylabel(names_max[1])
plt.show()

