import marcpy as mp

counter = 0

for i in range(0, 1000):
    counter += mp.binomialverteilt(1000, 0.005, i)
    if counter >= 0.99:
        print("\n", i)
        break

for i in range(0, 1000):
    counter += mp.binomialverteilt(1000, 0.00075, i)
    if counter >= 0.99:
        print("\n", i)
        break
