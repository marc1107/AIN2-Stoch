import statistics

import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
#import scipy.stats as stats

attrakt = [7, 4, 10, 10, 9, 3, 9, 6]
gehalt = [65, 60, 40, 70, 45, 40, 65, 55]
interessant = [3, 10, 9, 1, 5, 10, 2, 3]

print("1.11.1:")
print("Modalwert: ", stats.multimode(attrakt))
print("Mittelwert: ", np.mean(attrakt))
print("Standardabweichung", np.std(attrakt, ddof=1))
print("25%:", np.percentile(attrakt, 25))
print("50%:", np.percentile(attrakt, 50))
print("75%:", np.percentile(attrakt, 75))
print("60%:", np.percentile(attrakt, 60))

print("\n1.11.2:")
print("A,G:", np.corrcoef(attrakt, gehalt))
print("A,I:", np.corrcoef(attrakt, interessant))
print("G,I:", np.corrcoef(gehalt, interessant))