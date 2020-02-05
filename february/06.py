#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/5
"""
求1+2!+3!+...+20!的和
"""


def factorial(num):
    total = 1
    while num:
        total = total * num
        num -= 1
    return total


def sum_of_factorial(num):
    s = 0
    for i in range(1, num+1):
        s += factorial(i)
    return s


def sum_of_factorial2(num):
    s = 0
    total = 1
    for i in range(1, num + 1):
        total *= i
        s += total
    return s


def factorial2(num):
    if num == 1:
        return 1
    else:
        return num * factorial2(num - 1)


if __name__ == '__main__':
    print(sum_of_factorial(20))
    print(sum_of_factorial2(20))
    print(sum(map(factorial, range(1, 21))))
    print(factorial2(3))
