import numpy as np

N = 100000
totals = []

for i in range(N):
    t = 0
    c1 = 1
    c2 = 2

    while not (c1 == 3 and c2 == 4):
        flip1 = np.round(np.random.uniform(size=1))
        flip2 = np.round(np.random.uniform(size=1))
        if c2-c1 > 1:
            c1 += flip1
        if c2 < 4:
            c2 += flip2
        t += 1
    totals.append(t)
print(np.mean(totals))
print(np.std(totals))