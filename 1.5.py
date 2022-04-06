import numpy as np
import statistics as stat

list = [2, 4, 3, 1, 2, 4, 2, 2, 2, 3]

print("a)")
print(np.mean(list))

print("b)")
print(np.median(list))

print("c)")
print(stat.mode(list))

print("d)")
print(np.percentile(list, 10))

print("e)")
print(np.percentile(list, 25))

print("f)")
print(np.percentile(list, 75))

print("g)")
print(np.percentile(list, 75) - np.percentile(list, 25))

print("h)")
print(4-1)