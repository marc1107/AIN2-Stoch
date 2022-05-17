import numpy

print("b)")

x1 = [1, 1, 1, 1, 2, 3, 3, 3]
x2 = [1, 1, 1, 2, 2, 2, 3, 3]

print("x1: ", numpy.var(x1))
print("x2: ", numpy.var(x2))

print("\nc)")
print("x1: ", numpy.std(x1, ddof=1))
print("x2: ", numpy.std(x2, ddof=1))
