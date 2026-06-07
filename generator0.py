def my_generator():
    yield 2
    yield 3
    yield 4
    yield 5

for value in my_generator():
    print(value)