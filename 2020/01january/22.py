#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/31
"""
Problem 18: Write a program to print each line of a file in reverse order.
"""


def line_reverse(filename):
    with open(filename) as f:
        for line in f.readlines():
            print(line.rstrip()[::-1])
            print(' '.join(reversed(line[:-2].rstrip().split())))


if __name__ == '__main__':
    line_reverse('she.txt')
