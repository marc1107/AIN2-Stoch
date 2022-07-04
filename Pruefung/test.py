import numpy.random
import scipy

import marcpy as mp
import numpy.random as np

# Normalverteilung kumuliert
print(1 - scipy.stats.norm.cdf(120, 100, 15))
# Normalverteilung Einzelwerte
print(scipy.stats.norm.pdf([250], 300, 50))

print(scipy.stats.norm.cdf(110, 100, 15) - scipy.stats.norm.cdf(100, 100, 15))

print(scipy.stats.norm.ppf(0.99, 13, 1))

print("e)")
x = 0
for i in range(1, 100):
    x += mp.geomverteilt(i, 0.55)
    if x >= 1:
        print("i:", i)
        break


print("c)")
for i in range(650, 900):
    if mp.normalverteiltF(i, 700, 50) <= 0.9:
        print(i)
        break


print("Normal:")
print(scipy.stats.norm.ppf(0.9, 130, 15))

print("Welcher Wert wird nicht überschritten?")
for i in range(3, 100):
    if mp.expverteiltF(0.2, i) >= 0.9:
        print(i)
        print(mp.expverteiltF(0.2, i))
        break

print("Pruefung:")

