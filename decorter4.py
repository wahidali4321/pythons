def wahid(wahi):
    def inner():
        return wahi().upper()
    return inner

@wahid
def Strings():
    return "wahid ali khan will be a good AI engineers"

print(Strings())