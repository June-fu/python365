#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/20
"""
Problem 3:
Write a program to list all the files in the given directory along with their length and last modification time.
The output should contain one line for each file containing filename, length and modification date separated by tabs.

Hint: see help for os.stat.
"""


def file_stat(path):
    import os
    import time

    f_stat = []
    for file in os.listdir(path):
        st = os.stat(path + file)
        f_stat.append([file, st.st_size, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(st.st_mtime))])

    for s in f_stat:
        print(s[0], '\t', s[1] / 1024, 'kb', '\t', s[2])


if __name__ == '__main__':
    file_stat('./')
