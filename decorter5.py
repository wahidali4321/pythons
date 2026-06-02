def wahid(wahi):
    def inner():
        return wahi().lower()
    return inner

@wahid
def Strings():
    return "WAHID ALI WILL BE A GOOD AI ENGINEERS"

print(Strings())