import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

dauer = np.array([9, 13, 15, 18, 20])
gehalt = np.array([18000, 37000, 61000, 125000, 59000])

print("Korrelationskoeffizient:")
print(np.corrcoef(dauer, gehalt))

# Regression
slope, intercept, r, p, stderr = scipy.stats.linregress(dauer, gehalt)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'

fig, ax = plt.subplots()
ax.plot(dauer, gehalt, linewidth=0, marker='s', label='Data points')
ax.plot(dauer, intercept + slope * dauer, label=line)
ax.set_xlabel('Ausbildungsdauer X')
ax.set_ylabel('Jahresgehalt Y [1000€]')
ax.legend(facecolor='white')
plt.show()

