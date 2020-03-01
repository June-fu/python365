#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/1
"""
Problem 11: Write a python program zip.py to create a zip file.
The program should take name of zip file as first argument and files to add as rest of the arguments.

$ python zip.py foo.zip file1.txt file2.txt
"""


def my_zip(filename, *args):
    import zipfile

    with zipfile.ZipFile(filename, 'w') as zf:
        for f in args:
            zf.write(f)


if __name__ == '__main__':
    my_zip("foo.zip", "../january/01.py", "../january/02.py")
