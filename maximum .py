def maximum(a , b , c) :
    if a > b >c :
        return a + " is greater "
    elif b > a > c :
        return b + " is greater "
    else:
        return c + " is greater"
    
print(maximum(11 , 33 , 44))