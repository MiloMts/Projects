import math

def put_call_parity_diff(S, K, T, r, C, P):
    left = C - P
    right = S - K * math.exp(-r * T)
    return left - right

def check_put_call_parity(S, K, T, r, C, P, tol=1e-6):
    diff = put_call_parity_diff(S, K, T, r, C, P)
    return abs(diff) < tol, diff

S = 100
K = 100
T = 0.25
r = 0.03
C = 4.6
P = 3.8528054819

ok, diff = check_put_call_parity(S, K, T, r, C, P)
print("OK ?", ok)
print("diff =", diff)

ok, diff = check_put_call_parity(S, K, T, r, C, P)

if ok:
    print("No arbitrage (put-call parity holds).")
else:
    print("Arbitrage possible (put-call parity violated).")