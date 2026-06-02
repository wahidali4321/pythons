def started(wahi):
    def ended():
        return "Function Started"
    return wahi

@started
def lasted():
    return "Function Ended"

print(lasted())