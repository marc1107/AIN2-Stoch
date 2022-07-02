import numpy.random
import scipy

import marcpy as mp
import numpy.random as np

# Normalverteilung kumuliert
print(1 - scipy.stats.norm.cdf(120, 100, 15))
# Normalverteilung Einzelwerte
print(scipy.stats.norm.pdf([250], 300, 50))

print(scipy.stats.norm.cdf(110, 100, 15) - scipy.stats.norm.cdf(100, 100, 15))

for i in range(1, 100):
    print(mp.binhoechstens(mp.binomialverteilt(11, 0.55), i))
    if mp.binhoechstens(mp.binomialverteilt(11, 0.55), i) >= 1:
        print("Test")
        print(i)
        break
