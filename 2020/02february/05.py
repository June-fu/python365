#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/4
"""
一、如何打印出想要的图案（菱形）
二、2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""


# use center() function
from functools import reduce


def diamond(side_len):
    for i in range(1, side_len + 1, 2):
        print((i * '*').center(side_len, ' '))
    for i in reversed(range(1, side_len, 2)):
        print((i * '*').center(side_len, ' '))


# 先生成两个队列，然后同时遍历，计算数列和
def sum_of_nums(num):
    lst = [1, 2]
    lst2 = [2, 3]
    total = 0
    for i in range(2, num):
        lst.append(lst[i-1] + lst[i-2])
        lst2.append(lst2[i - 1] + lst2[i - 2])
    for x, y in zip(lst2, lst):
        total += x/y
    # print(reduce(lambda m, n: m+n, [x/y for x, y in zip(lst2, lst)]))
    return total


def sum_of_nums2(num):
    a = 2.0
    b = 1.0
    total = 0
    for i in range(num):
        total += a/b
        a, b = a + b, a
    return total


if __name__ == '__main__':
    diamond(7)
    print(sum_of_nums(20))
    print(sum_of_nums2(20))
