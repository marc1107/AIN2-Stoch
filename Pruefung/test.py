import numpy.random
import scipy

import marcpy as mp
import numpy.random as np

# Normalverteilung kumuliert
print(1 - scipy.stats.norm.cdf(120, 100, 15))
# Normalverteilung Einzelwerte
print(scipy.stats.norm.pdf([250], 300, 50))

print(scipy.stats.norm.cdf(110, 100, 15) - scipy.stats.norm.cdf(100, 100, 15))


print("e)")
x = 0
for i in range(1, 100):
    x += mp.geomverteilt(i, 0.55)
    if x >= 1:
        print("i:", i)
        break
