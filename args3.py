def summation(*numbers):
    total = 0

    for x in numbers:
        total += x

    return total

print(summation(10, 20, 30, 40))