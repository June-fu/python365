#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/18
"""
Problem 37: Write a function value_sort to sort values of a dictionary based on the key.
"""


def value_sort(dict1):
    return [x[1] for x in sorted(dict1.items(), key=lambda item: item[0])]


# Sort a dictionary by value
def v_sort(dict2):
    return {k: v for k, v in sorted(dict2.items(), key=lambda item: item[1])}


if __name__ == '__main__':
    my_dict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    print(value_sort(my_dict))
    print(v_sort(my_dict))
