def myFunction(n):
    return lambda a : a *n

mydoubler = myFunction(2)
print(mydoubler(11))