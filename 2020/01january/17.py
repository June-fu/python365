# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/29
"""
Problem 16: Write a function ext_sort to sort a list of files based on extension.
input: ext_sort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
output: ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
"""


def ext_sort(list1):
    list1.sort(key=lambda x: x.split('.')[1])
    return list1


if __name__ == '__main__':
    n = ext_sort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    print(n)
