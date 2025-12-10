import numpy as np
from scipy.stats import norm

def bs_d1_d2(S, K, T, r, sigma):
    S = np.asarray(S)
    K = np.asarray(K)
    T = np.asarray(T)
    r = np.asarray(r)
    sigma = np.asarray(sigma)
    
    sqrtT = np.sqrt(T)
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*sqrtT)
    d2 = d1 - sigma*sqrtT
    return d1, d2

def black_scholes_call(S, K, T, r, sigma):
    d1, d2 = bs_d1_d2(S, K, T, r, sigma)
    return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

def black_scholes_put(S, K, T, r, sigma):
    d1, d2 = bs_d1_d2(S, K, T, r, sigma)
    return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def delta_call(S, K, T, r, sigma):
    d1, _ = bs_d1_d2(S, K, T, r, sigma)
    return norm.cdf(d1)

def delta_put(S, K, T, r, sigma):
    d1, _ = bs_d1_d2(S, K, T, r, sigma)
    return norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    d1, _ = bs_d1_d2(S, K, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

# vega per 1 unit of volatility (i.e. per 100% change)
def vega(S, K, T, r, sigma):
    d1, _ = bs_d1_d2(S, K, T, r, sigma)
    return S * norm.pdf(d1) * np.sqrt(T)

# theta per year
def theta_call(S, K, T, r, sigma):
    d1, d2 = bs_d1_d2(S, K, T, r, sigma)
    
    term1 = -S * norm.pdf(d1) * sigma / (2*np.sqrt(T))
    term2 = -r * K * np.exp(-r*T) * norm.cdf(d2)
    return term1 + term2

def theta_put(S, K, T, r, sigma):
    d1, d2 = bs_d1_d2(S, K, T, r, sigma)
    
    term1 = -S * norm.pdf(d1) * sigma / (2*np.sqrt(T))
    term2 = r * K * np.exp(-r*T) * norm.cdf(-d2)
    return term1 + term2

def rho_call(S, K, T, r, sigma):
    _, d2 = bs_d1_d2(S, K, T, r, sigma)
    return K * T * np.exp(-r*T) * norm.cdf(d2)

def rho_put(S, K, T, r, sigma):
    _, d2 = bs_d1_d2(S, K, T, r, sigma)
    return -K * T * np.exp(-r*T) * norm.cdf(-d2)

times = np.linspace(0, 1, 100)
print(np.round(black_scholes_call(100, 105, times, 0.03, 0.2), 3))