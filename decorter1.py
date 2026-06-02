def started(wahi):
    def ended():
        return "Function Started"
    return ended

@started
def lasted():
    return "Function Ended"

print(lasted())