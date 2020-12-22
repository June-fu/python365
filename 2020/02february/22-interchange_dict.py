#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/18
"""
Problem 38: Write a function invert_dict to interchange keys and values in a dictionary.
For simplicity, assume that all values are unique.

>>> invert_dict({'x': 1, 'y': 2, 'z': 3})
{1: 'x', 2: 'y', 3: 'z'}
"""


def invert_dict(dct):
    return {v: k for k, v in dct.items()}


# if the values of the dict is not unique
def invert_dict2(dct):
    d = {}
    for k, v in dct.items():
        if v not in d.keys():
            d[v] = k
        elif type(d[v]) is list:
            d[v].append(k)
        else:
            d[v] = [d[v], k]
    return d


if __name__ == '__main__':
    a = {'x': 1, 'y': 2, 'z': 3}
    b = {'x': 1, 'y': 2, 'z': 3, 't': 3}
    print(invert_dict(a))
    print(invert_dict2(b))
