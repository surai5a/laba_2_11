#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func1(a, b):
    x = a
    y = b

    def func2():
        nonlocal x, y
        return f"Для значений {x}, {y} функция f({x},{y}) = {x + y}"
    return func2


a = int(input("a? "))
b = int(input("b? "))
test = func1(a, b)
print(test())

