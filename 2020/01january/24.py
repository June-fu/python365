#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/31
"""
Problem 20: Implement unix command grep.
The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

input: python grep.py she.txt sure
output: The shells that she sells are seashells I'm sure.
        I'm sure that the shells are seashore shells.
"""


def grep(filename, str1):
    with open(filename) as f:
        lst = []
        for line in f.readlines():
            if str1 in line:
                lst.append(line)
        return ''.join(lst)


if __name__ == '__main__':
    import sys
    file_name, string = sys.argv[1], sys.argv[2]
    print(grep(file_name, string))
