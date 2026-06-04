def countdown(n):
    if n < 1 :
        return
    print(n)

    countdown(n - 1)

countdown(5)