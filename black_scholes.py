import math

def norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def black_scholes_price(S, K, T, r, sigma, option_type):
    if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
        raise ValueError("S, K, T, sigma doivent être > 0")

    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    discount = math.exp(-r * T)

    if option_type.lower() == "call":
        return S * norm_cdf(d1) - K * discount * norm_cdf(d2)

    if option_type.lower() == "put":
        return K * discount * norm_cdf(-d2) - S * norm_cdf(-d1)

    raise ValueError("option_type doit être 'call' ou 'put'")

S = 100
K = 110
T = 0.5
r = 0.03
sigma = 0.20

call_price = black_scholes_price(S, K, T, r, sigma, "call")
put_price  = black_scholes_price(S, K, T, r, sigma, "put")

print("Call price =", round(call_price, 4))
print("Put price  =", round(put_price, 4))
