#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/31
"""
Problem 23: Write a program center_align.py to center align all lines in the given file.
input:python center_align.py she.txt
  I'm sure that the shells are seashore shells.
    So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
       She sells seashells on the seashore;
"""


def center_align(filename):
    with open(filename) as f:
        lst_file = f.readlines()
        lst = [len(x) for x in lst_file]
        max_len = max(lst)
        middle = [int((max_len - y)/2 + y) for y in lst]

        for i, line in zip(range(len(lst_file)), lst_file):
            # this is the core
            lst_file[i] = line[:-1].ljust(middle[i], ' ').rjust(max_len, ' ') + '\n'
        return ''.join(lst_file)


# use center() function
def center_align2(filename):
    with open(filename) as f:
        lst_file = f.readlines()

        for line in lst_file:
            print(line[:-1].center(max([len(x) for x in lst_file]), ' '))


if __name__ == '__main__':
    print(center_align('she.txt'))
    print(center_align2('she.txt'))

