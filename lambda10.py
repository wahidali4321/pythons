def myFunction(n) :
    return lambda a : a + n

mydoubler = myFunction(10)

print(mydoubler(11))