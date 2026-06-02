def Star(func):
    def inner():
        print("**********")
        func()
        print("**********")
    return inner

@Star
def function():
    print("Hello World")

function()