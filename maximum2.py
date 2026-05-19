def maximum(a , b , c) :
    if a > b >c :
        return str(a)+ " is greater "
    elif b > a > c :
        return str(b) + " is greater "
    else:
        return str(c) + " is greater"
    
print(maximum(11 , 33 , 44))
print(maximum(11, 11 , 11))