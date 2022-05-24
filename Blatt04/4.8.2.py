import numpy as np

x1 = [1, 1, 2, 2, 3, 3]

print("Varianz X1:", np.var(x1))
print("Std X1:", np.std(x1, ddof=1))
