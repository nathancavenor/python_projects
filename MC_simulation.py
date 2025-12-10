import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

N = 1000 #no of paths
M = 1000 #no of time steps
S0 = 50
sigma = 0.2
dt = 1/365
T = M*dt
r = 0.03

paths = np.zeros((N, M+1))
paths[:, 0] = S0

for t in range(1, M+1):
    Z = np.random.randn(N)
    paths[:, t] = paths[:, t-1] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)

time_grid = np.linspace(0, T, M+1)

plt.figure(figsize=(10,6))

plt.plot(time_grid, paths.T, color='grey', lw=1, alpha=0.4)

plt.plot(time_grid, paths.mean(axis=0), color='black', lw=2, label='Mean path')

plt.xlabel("Time (years)")
plt.ylabel("Stock Price")
plt.title("Monte Carlo Simulated GBM Paths")
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.show()

