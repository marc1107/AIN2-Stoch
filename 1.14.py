import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# Arrays mit Daten füllen
cargocap = [3000000, 36000000, 180000, 1000000000000, 100000, 110, 110, 250000000]
costs = [3500000, 150000000, 240000, 1000000000000, 100000, 134999, 149999, 1143350000]
costs_s = [3500000, 150000000, 240000, 100000, 134999, 149999]
speed = [950, 975, 1000, 1050, 1000, 1050]
spaceships = ["CR90", "Star Des", "Sentinel", "Death", "Falcon", "Y-wing", "X-wing", "Executor"]
spaceships2 = ["CR90", "Star Des", "Sentinel", "Falcon", "Y-wing", "X-wing"]
cargo_cost = np.empty(len(cargocap), dtype=float)
speed_cost = np.empty(len(speed), dtype=float)

# Berechnung Cargo/Credit
for i in range(0, len(cargocap)):
    cargo_cost[i] = round(cargocap[i] / costs[i], 4)

# Brechnung >Speed/Credit
for i in range(0, len(speed)):
    speed_cost[i] = round(speed[i] / costs_s[i], 4)

# Mittelwert, Median und Standardabweichung
mi = np.mean(costs)
me = np.median(costs)
std = np.std(costs)
print("Mittelwert: ", mi, "\nMedian: ", me, "\nStandardabweichung: ", std)
costs = [mi, me, std]
b = sb.boxplot(costs)
b.set_ylabel("Kosten")
b.set_xlabel("[x100mio]")

plt.show()

# Werte direkt bei den Punkten anzeigen
fig, ax = plt.subplots()
ax.scatter(spaceships, cargo_cost)
ax.set_ylabel("cargo/credit")

for i, txt in enumerate(cargo_cost):
    ax.annotate(txt, (spaceships[i], cargo_cost[i]))

#plt.scatter(spaceships, cargo_cost)
plt.title("cargo capacity per credit")
plt.show()

# Werte direkt bei den Punkten anzeigen
fig, ax = plt.subplots()
ax.scatter(spaceships2, speed_cost)
ax.set_ylabel("speed/credit")

for i, txt in enumerate(speed_cost):
    ax.annotate(txt, (spaceships2[i], speed_cost[i]))

plt.title("speed per credit")
plt.show()