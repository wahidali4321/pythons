def my_generator():
    yield 10
    yield 20
    yield 32
    yield 44

for value in my_generator():
    print(value)