#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/31
"""
Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
input: python wrap.py she.txt 30
I'm sure that the shells are s
eashore shells.
So if she sells seashells on t
he seashore,
The shells that she sells are
seashells I'm sure.
She sells seashells on the sea
shore;
"""


def wrap(filename, width):
    lst = []
    with open(filename) as f:
        for line in f.readlines():
            if len(line) > width:
                lst.append(line[:width] + '\n' +line[width:])
            else:
                lst.append(line)
    return ''.join(lst)


if __name__ == '__main__':
    import sys
    file_name, w = sys.argv[1], sys.argv[2]

    print(wrap(file_name, int(w)))
