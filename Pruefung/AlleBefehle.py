import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
import scipy.stats as stats

# Array erstellen:
list = [2, 4, 3, 1, 2, 4, 2, 2, 2, 3]
# Numpy Array erstellen:
nparray1 = np.array([9, 13, 15, 18, 20])
nparray2 = np.array([18000, 37000, 61000, 125000, 59000])

# Mittelwert berechnen:
mean = np.mean(list)

# Median berechnen:
median = np.median(list)

# Modalwert berechnen (hier kann es mehrere geben, gibt Array zurück):
mode = stats.multimode(list)
# Modalwert berechnen (wenn es genau 1 ist, unschön!):
mode = stat.mode(list)

# Quantile (bzw. Percentile) berechnen:
percentile = np.percentile(list, 25)  # geht auch mit 10 usw.

# Interquartilabstand berechnen:
interquartile = np.percentile(list, 75) - np.percentile(list, 25)

# Spannweite berechnen:
if len(list) > 0:
    list.sort()
    span = list[len(list) - 1] - list[0]

# empirische Standardabweichung berechnen:
std = np.std(list, ddof=1)

# Variant berechnen:
varianz = np.var(list)

# Korrelationskoeffizienten berechnen:
corrcoef = np.corrcoef(nparray1, nparray2)

# lineare Reggressionsfunktion:
slope, intercept, r, p, stderr = stats.linregress(nparray1, nparray2)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'

# Punkte von Array und Reggressionslinie mit Legende plotten:
fig, ax = plt.subplots()
ax.plot(nparray1, nparray2, linewidth=0, marker='s', label='Data points')
ax.plot(nparray1, intercept + slope * nparray1, label=line)
ax.set_xlabel('Ausbildungsdauer X')
ax.set_ylabel('Jahresgehalt Y [1000€]')
ax.legend(facecolor='white')
plt.show()

# for each Schleife (z. B. aufaddieren):
sum = 0
for number in list:
    sum += number

# for Schleife wie in Java
sum = 0
for i in range(0, len(list)):
    sum += list[i]


# Funktion/Methode erstellen (hier z.B. Fakultät):
def fak(n: int):
    if n > 0:
        return n * fak(n - 1)
    else:
        return 1
