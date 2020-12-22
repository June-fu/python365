#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/2
"""
Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets
such that sum of first two elements of the triplet equals the third element using numbers below n.
Please note that (a, b, c) and (b, a, c) represent same triplet.

>>> triplets(5)
[(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
"""


def triplets(num):
    return [(i, j, k) for i in range(1, num) for j in range(i, num) for k in range(j, num) if i + j == k]


if __name__ == '__main__':
    print(triplets(5))
