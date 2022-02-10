def func1(a, b):
    x = a
    y = b

    def func2():
        nonlocal x, y
        return x + y
    return func2


test = func1(5, 6)
print(test())

