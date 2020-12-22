#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/31
"""
Write a program reverse(filename) to print lines of a file in reverse order
"""


# Number of characters in a file
import sys


def char_count(filename):
    return len(open(filename).read())


# Number of words in a file
def word_count(filename):
    return len(open(filename).read().split())


# Number of lines in a file
def line_count(filename):
    return len(open(filename).readlines())


# Write a program reverse.py to print lines of a file in reverse order
def reverse(filename):
    with open(filename) as f:
        lst = f.readlines()
        lst.reverse()
        for i in lst:
            print(i.rstrip())


if __name__ == '__main__':
    print(char_count('she.txt'))
    print(word_count('she.txt'))
    print(line_count('she.txt'))

    reverse('she.txt')

    for line in reversed(open('she.txt').readlines()):
        print(line.rstrip())
