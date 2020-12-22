#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/1
"""
判断101-200之间有多少个素数，并输出所有素数。
"""


def is_prime(num):
    for i in range(2, num):
        if num % i:
            continue
        else:
            return True
    return False


if __name__ == '__main__':
    total = 0
    for j in range(101, 201):
        if not is_prime(j):
            print(j)
            total += 1
    print('The total is %d' % total)
