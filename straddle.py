import numpy as np

K = 100
call_premium = 6
put_premium = 4

S = np.arange(50, 151, 1) 

call_payoff = np.maximum(S - K, 0)
put_payoff = np.maximum(K - S, 0)

straddle_pl = call_payoff + put_payoff - (call_premium + put_premium)

total_premium = call_premium + put_premium
be_low = K - total_premium
be_high = K + total_premium

print(f"Strike K = {K}")
print(f"Call premium = {call_premium}, Put premium = {put_premium}")
print(f"Straddle break-even low  = {be_low}")
print(f"Straddle break-even high = {be_high}")
print(f"Max loss (at S_T=K)      = {-total_premium}")
