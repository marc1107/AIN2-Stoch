import scipy.stats as stats

# a)
print(1 - stats.norm.cdf(120, 100, 15))

# b)
print(stats.norm.cdf(110, 100, 15) - stats.norm.cdf(100, 100, 15))

# c)
hoherIQ = 150
# von hohem IQ nach niedrigem IQ zählen
for i in range(0, hoherIQ):
    if (1 - stats.norm.cdf(hoherIQ - i, 100, 15)) > 0.1:
        print(hoherIQ - i + 1)
        break

# d)
for i in range(0, hoherIQ):
    if (1 - stats.norm.cdf(hoherIQ - i, 100, 15)) >= 0.99:
        print(hoherIQ - i)
        break