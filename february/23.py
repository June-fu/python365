#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/19
"""
Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.

$ python extcount.py src/
14 py
4 txt
1 csv
"""


def extcount(path):
    import os
    d = {}
    for file in os.listdir(path):
        k = file.split('.')[-1]
        d[k] = d.get(k, 0) + 1
    for k, v in d.items():
        print(v, k)


if __name__ == '__main__':
    extcount('./')

