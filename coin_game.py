import numpy as np

N = 10000
T = 10
f = 1
S0 = 1

paths = np.zeros((N, T+1))
paths[:, 0] = S0

for t in range(1, T+1):
    coins = np.round(np.random.uniform(size = N))
    paths[:, t] = coins * (paths[:,t-1]*(1+2*f)) + (np.ones(N)-coins)*(paths[:, t-1]*(1-f))

print(np.mean(paths[:,-1]))
print(np.std(paths[:, -1]))