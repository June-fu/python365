#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/13
"""
How to make a flat list out of list of lists?
https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
# Flatten one level of nesting
lst = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
output:
"""


def flat1(lst):
    return [item for sublist in lst for item in sublist]


def flat2(lst):
    return sum(lst, [])


def flat3(lst):
    from itertools import chain
    return list(chain.from_iterable(lst))


def flat4(lst):
    import functools
    import operator
    return functools.reduce(operator.iconcat, lst, [])


def flat5(lst):
    import numpy
    return list(numpy.concatenate(lst))


# the same as flat3, using setuptools
def flat6(lst):
    from setuptools.namespaces import flatten
    return flatten(lst)


# using pandas
def flat7(lst):
    from pandas.core.common import flatten
    return list(flatten(lst))


# using matplotlib
def flat8(lst):
    from matplotlib.cbook import flatten
    return list(flatten(lst))


# using unipath
def flat9(lst):
    from iteration_utilities import deepflatten
    return list(deepflatten(lst))


# using nltk
def flat10(lst):
    from nltk import flatten
    return flatten(lst)


if __name__ == '__main__':
    L = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
    print("flat1:", flat1(L))
    print("flat2:", flat2(L))
    print("flat3:", flat3(L))
    print("flat4:", flat4(L))
    print("flat5:", flat5(L))
    print("flat6:", flat6(L))
    print("flat7:", flat7(L))
    print("flat8:", flat8(L))
    print("flat9:", flat9(L))
    print("flat10:", flat10(L))
