#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/31
"""
https://anandology.com/python-practice-book/working-with-data.html#sets
Problem 19: Implement unix commands head and tail.
The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
"""


def head(filename):
    with open(filename) as f:
        i = 0
        for line in f.readlines():
            if i < 10:
                print(line.rstrip())
            i += 1


# should use this function
def head1(filename):
    with open(filename) as f:
        return ''.join(f.readlines()[:10])


def tail(filename):
    with open(filename) as f:
        lst = f.readlines()
        length = len(lst)
        if length < 10:
            for line in lst:
                print(line.rstrip())
        else:
            for i in reversed(range(1, 11)):
                print(lst[length - i].rstrip())


# should use this function
def tail1(filename):
    with open(filename) as f:
        return ''.join(f.readlines()[-10:])


if __name__ == '__main__':
    head('she.txt')
    tail('she.txt')

    # import sys
    # file_name = sys.argv[1]
    print(head1('she.txt'))
    print(tail1('she.txt'))
