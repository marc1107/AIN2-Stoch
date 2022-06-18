# Program for all the commands used in Stochastik
import math

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
    print("Array muss mindestens 1 Zahl beinhalten!")
    return 0


def std(arr):
    return np.std(arr, ddof=1)


def var(arr):
    return np.var(arr)


def corrcoef(arr1, arr2):
    return np.corrcoef(arr1, arr2)


def fak(n: int, x: int):
    if n > 0:
        return n * fak(n - 1)
    else:
        return 1


def fak(n: int):
    if n > 0:
        ergebnis = n
        for i in range(1, n):
            ergebnis = ergebnis * (n-i)
    else:
        return 1

    return ergebnis


def linregress(arr1, arr2):
    # Convert to numpy array
    nparr1 = np.asarray(arr1)
    nparr2 = np.asarray(arr2)
    return scipy.stats.linregress(nparr1, nparr2)


def plotlinregress(narr1, narr2, lbl_x, lbl_y):
    # Convert to numpy array
    arr1 = np.asarray(narr1)
    arr2 = np.asarray(narr2)

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


# Liefert ein mehrdimensionales Array zurück.
# Für jeden Eintrag ist der erste Eintrag die Zahl und der zweite die zugehörige Häufigkeit
def abs_haeufigkeit(arr):
    absolute = []
    if len(arr) > 0:
        arr_sorted = []
        # Array Einträge kopieren, ohne das richtige Array zu verändern
        for i in arr:
            arr_sorted.append(i)
        arr_sorted.sort()

        number = arr_sorted[0]
        counter = 0
        for i in arr_sorted:
            if number != i:
                absolute.append([number, counter])
                number = i
                counter = 1
            else:
                counter += 1

        absolute.append([number, counter])

    return absolute


def rel_haeufigkeit(arr):
    rel = []
    if len(arr) > 0:
        absolute = abs_haeufigkeit(arr)
        ges = 0
        for i in absolute:
            ges += i[1]

        for i in absolute:
            number = i[0]
            reldiv = i[1]/ges
            rel.append([number, reldiv])

    return rel


def kum_haeufigkeit(arr):
    kum = []
    if len(arr) > 0:
        rel = rel_haeufigkeit(arr)
        kum_counter = 0
        for i in rel:
            number = i[0]
            kum_counter += i[1]
            kum.append([number, kum_counter])

    return kum


def bincoef(n: int, k: int):
    return fak(n)/(fak(k)*fak(n-k))


def bernoulliverteilt(p: float):
    q = 1 - p
    arr = [[1, p], [0, q]]
    return arr


def bernoullierwartung(p: float):
    return p


def bernoullivar(p: float):
    q = 1 - p
    return p * q


# gibt Array mit allen binomial verteilten Werten von 0 bis n zurück
# also alle möglichen t's (immer die ersten Werte im mehrdimensionalen Array)
def binomialverteilt(n: int, p: float):
    arr = []
    q = 1 - p
    if n > 0:
        for t in range(0, n+1):
            arr.append([t, bincoef(n, t) * pow(p, t) * pow(q, n-t)])
    return arr


def binomialverteilt1(n: int, p: float, t: int):
    result = 0
    q = 1 - p
    if n > 0:
        result = bincoef(n, t) * pow(p, t) * pow(q, n-t)
    return result


def binerwartung(n: int, p: float):
    return n * p


def binvar(n: int, p: float):
    return n * p * (1 - p)


def binmindestens(arr, x: int):
    result = 0
    for pack in arr:
        if pack[0] >= x:
            result += pack[1]
    return result


def binhoechstens(arr, x: int):
    result = 0
    for pack in arr:
        if pack[0] <= x:
            result += pack[1]
    return result


def binminhoe(arr, x: int, y: int):
    result = 0
    for pack in arr:
        if x <= pack[0] <= y:
            result += pack[1]
    return result


# Noch nicht fertig!!!
def geomverteilt(x: int, p: float):
    q = 1 - p
    return p * pow(q, x - 1)


def geomerwartung(p: float):
    return 1/p


def geomvar(p: float):
    return (1 - p) / math.sqrt(p)


def poissonverteilt(x: int, lbd):
    e = math.e
    return pow(lbd, x) / fak(x) * pow(e, -lbd)

