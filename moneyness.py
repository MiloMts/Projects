def moneyness(S, K, option_type="call"):
    option_type = option_type.lower()
    
    if option_type == "call":
        if S > K:
            return "ITM"
        elif S < K:
            return "OTM"
        else:
            return "ATM"
    
    elif option_type == "put":
        if S > K:
            return "OTM"
        elif S < K:
            return "ITM"
        else:
            return "ATM"
    
    else:
        return "Option type must be 'call' or 'put'"

print(moneyness(80, 110, "call"))

