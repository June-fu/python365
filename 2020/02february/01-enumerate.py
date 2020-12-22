#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/2
"""
Problem 28: Write a function enumerate that takes a list
and returns a list of tuples containing (index,item) for each item in the list.

>>> enumerate(["a", "b", "c"])
[(0, "a"), (1, "b"), (2, "c")]
>>> for index, value in enumerate(["a", "b", "c"]):
...     print(index, value)
0 a
1 b
2 c

Problem 29: Write a function array to create an 2-dimensional array.
The function should take both dimensions as arguments. Value of each element can be initialized to None:
>>> a = array(2, 3)
[[None, None, None], [None, None, None]]

Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.
input: parse_csv('a.csv')
[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
"""


def enumerate1(lst):
    return[(i, j) for i, j in zip(range(len(lst)), lst)]


def array(row, column):
    return [[None for i in range(column)] for j in range(row)]


def parse_csv(filename):
    with open(filename) as f:
        return [line.rstrip().split() for line in f.readlines()]


def parse_csv2(filename, delimiter, comment):
    with open(filename) as f:
        return [line.rstrip().split(delimiter) for line in f.readlines() if not line.startswith(comment)]


if __name__ == '__main__':
    print(enumerate1(["a", "b", "c"]))
    for index, value in enumerate(["a", "b", "c"]):
        print(index, value)

    print(array(2, 3))
    print(parse_csv('a.csv'))

