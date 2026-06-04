def factorial(n):
    if n == 1 :
        return 1
    return  n * factorial_recursive(n - 1)

print(factorial(5))