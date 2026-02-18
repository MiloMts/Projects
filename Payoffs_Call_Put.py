def payoff_calls(S_T, K):
    return max(S_T - K,0)
def payoff_puts(S_T, K):
    return max(K - S_T,0)
print(payoff_calls(115,100))
print(payoff_puts(80,100))