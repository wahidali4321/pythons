def wahid(func):
    def inner():
        return func().upper()
    return inner

@wahid
def myFunction():
    return "wahid ali is very good boy"

print(myFunction())