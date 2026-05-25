def Changecase(func):

    def myinner():
        return func().upper()
    
    return myinner

@Changecase
def myFunction():
    return "Hello wahid ali khan!"

print(myFunction())