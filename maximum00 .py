def maximum(a, b, c):
    if a > b and a > c:
        return str(a) + " is greater"
    
    elif b > a and b > c:
        return str(b) + " is greater"
    
    else:
        return str(c) + " is greater"

print(maximum(11, 33, 44))