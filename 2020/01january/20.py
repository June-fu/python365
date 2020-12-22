#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/30
"""
输入三个整数x,y,z，请把这三个数由小到大输出。
斐波那契数列
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""


def sort_num(x, y, z):
    x1 = x
    y1 = y
    z1 = z
    lst = [x1, y1, z1]
    lst.sort()
    for i in lst:
        print(i)


def fib(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def fib2(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib2(n - 1) + fib2(n - 2)


if __name__ == '__main__':
    x, y, z = 5, 9, 8
    sort_num(x, y, z)

    print(fib(3))
    print(fib2(3))
