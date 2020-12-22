#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/31
"""
itertools — Functions creating iterators for efficient looping
The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.

Infinite iterators:
count(start=0, step=1) --> start, start+step, start+2*step, ...
cycle(p) --> p0, p1, ... plast, p0, p1, ...
repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times

"""


def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step


def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    while True:
        for element in iterable:
            yield element


def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times:
        for i in range(times):
            yield object
    else:
        while True:
            yield object


if __name__ == '__main__':
    a = cycle('ABCD')
    print([a.__next__() for i in range(10)])

    print([i for i in repeat(10, 3).__iter__()])

    # A common use for repeat is to supply a stream of constant values to map or zip:
    b = map(pow, range(10), repeat(2))
    print(list(b))
