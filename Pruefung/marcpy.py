# Program for all the commands used in Stochastik

import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import scipy.stats


def mean(arr):
    return np.mean(arr)


def median(arr):
    return np.median(arr)


def mode(arr):
    return stats.multimode(arr)


def percentile(arr, p: int):
    return np.percentile(arr, p)


def interquartilediff(arr):
    return np.percentile(arr, 75) - np.percentile(arr, 25)


def span(arr):
    if len(arr) > 0:
        arr.sort()
        return arr[len(arr) - 1] - arr[0]
    return 0


def std(arr):
    return np.std(arr, ddof=1)


def var(arr):
    return np.var(arr)


def corrcoef(arr1, arr2):
    return np.corrcoef(arr1, arr2)


def linregress(arr1, arr2):
    return scipy.stats.linregress(arr1, arr2)


def plotlinregress(arr1, arr2, lbl_x, lbl_y):
    slope, intercept, r, p, stderr = linregress(arr1, arr2)
    line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'

    # Punkte von Array und Reggressionslinie mit Legende plotten:
    fig, ax = plt.subplots()
    ax.plot(arr1, arr2, linewidth=0, marker='s', label='Data points')
    ax.plot(arr1, intercept + slope * arr1, label=line)
    ax.set_xlabel(lbl_x)
    ax.set_ylabel(lbl_y)
    ax.legend(facecolor='white')
    plt.show()


nparray1 = np.array([9, 13, 15, 18, 20])
nparray2 = np.array([18000, 37000, 61000, 125000, 59000])
plotlinregress(nparray1, nparray2, 'Ausbildungsdauer X', 'Jahresgehalt Y [1000€]')
