def Star(name):
    def inner():
        print("**********")
    return inner

@Star
def function():
    print("**********")

function()