#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/2
"""
编程找出1000以内的所有完数。
完数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
6 [1, 2, 3]
28 [1, 2, 4, 7, 14]
496 [1, 2, 4, 8, 16, 31, 62, 124, 248]
"""
from functools import reduce


# def approximation(num):
#     lst = []
#     for x in range(1, num):
#         if not num % x:
#             lst.append(x)
#     return lst


def approximation(num):
    return [x for x in range(1, num) if not num % x]


def is_perfect_number(num):
    if num == reduce(lambda x, y: x + y, approximation(num)):
        return True
    else:
        return False


def is_perfect_number2(num):
    if num == reduce(lambda x, y: x + y, [x for x in range(1, num) if not num % x]):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_perfect_number(28))
    for i in range(2, 1001):
        if is_perfect_number(i):
            print(i, approximation(i))

    for i in range(2, 1001):
        if is_perfect_number2(i):
            print(i)
