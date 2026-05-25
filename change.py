def changcase(func):

    def myinner():
        return func().upper()

    return myinner


@changcase
def myFunction():
    return "Hello wahid ali"


print(myFunction())