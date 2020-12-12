#!/usr/bin/python
"""
Print a single base-10 integer that denotes the maximum number of 
consecutive 1's in the binary representation of n.
https://www.hackerrank.com/challenges/30-binary-numbers/problem
"""
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    result = ''
    while n:
        result += str(n % 2)
        n = n // 2
    lst = result.split('0')
    print(max(len(i) for i in lst))

# print(len(max(bin(n)[2:].split('0'))))