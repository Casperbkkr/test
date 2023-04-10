#!/usr/bin/env python3
import numpy as np
import math as mt
import matplotlib.pyplot as plt


# parameters
T = 10
K = 10
r = 0.06
sigma = 0.5
A = 20


# define functions to calculate value of delta of call
def a(t: np.array) -> np.array:
	return sigma * np.sqrt(2 * (T - t))


def x(t: np.array, S: np.array) -> np.array:
	return np.log(S / K) + (r - ((sigma ** 2) / 2)) * (T - t)


def Dirac(t: np.array, S: np.array) -> np.array:
	return (a(t) * np.sqrt(mt.pi)) ** (-1) * np.exp((-1) * (x(t, S) / a(t)) ** 2)


def C(t: np.array, S: np.array) -> np.array:
	return (A * np.exp((-1) * r * (T - t))) / S


def Delta(t: np.array, S: np.array) -> np.array:
	return C(t, S) * Dirac(t, S)


# define input matrices
S = np.linspace(0, 2 * K, 10001)
S = np.vstack([S for i in range(10)])
t = np.array([1 / (10 ** i) for i in range(10)])
t = np.vstack([T - t for i in range(10001)])
t = t.T
out = (Delta(t, S)).T

# plot delta vs moneyness without axis ticks.
plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(111)

# only plot for the smallest difference between T and t
ax.plot(S[0, :], out[:, -1])

# set title and labels
fig.suptitle(r"Value of $\Delta$ for $t\rightarrow T$")
plt.ylabel(r"$\Delta(t)$")
plt.xlabel(r"$S(t)$")

# set axes to blank except for K
plt.tick_params(axis='y', labelleft=False)
xticks = ax.xaxis.get_major_ticks()
tick_lables = ax.get_xticklabels()
tick_lables[5] = "K"
ax.set_xticklabels(tick_lables)
# set all label to invisible
for i in range(len(xticks)):
	xticks[i].label1.set_visible(False)
# set the middle tick to visible
middle_index = len(xticks) // 2
xticks[middle_index].label1.set_visible(True)

# show plot
plt.show()
