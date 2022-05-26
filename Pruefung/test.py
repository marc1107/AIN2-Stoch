import marcpy as mp

counter = 0

for i in range(0, 1000):
    counter += mp.binomialverteilt(1000, 0.005, i)
    if counter >= 0.99:
        print("\n", i)
        break

# Test