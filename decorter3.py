def started(wahi):
    def ended():
        print("Function Started")
        wahi()
        print("Function Finished")
    return ended

@started
def lasted():
    print("Welcome to Python")

lasted()