#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/2
"""
Problem 25: Provide an implementation for map using list comprehensions.
>>> def square(x): return x * x
...
>>> map(square, range(5))
[0, 1, 4, 9, 16]

Problem 26:Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true.
Provide an implementation for filter using list comprehensions.
>>> def even(x): return x %2 == 0
...
>>> filter(even, range(10))
[0, 2, 4, 6, 8]
"""


def square(x):
    return x * x


def even(x):
    return x % 2 == 0


def my_map(func, iter1):
    return [func(x) for x in iter1]


def my_filter(f, a):
    return [x for x in a if f(x)]


if __name__ == '__main__':
    print(my_map(square, range(5)))
    print(my_filter(even, range(10)))
