#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/2
"""
Problem 12: Write a program mydoc.py to implement the functionality of pydoc.
The program should take the module name as argument and
print documentation for the module and each of the functions defined in that module.

    $ python mydoc.py os
    Help on module os:

    DESCRIPTION

    os - OS routines for Mac, NT, or Posix depending on what system we're on.
    ...

    FUNCTIONS

    getcwd()
        ...
"""

# Hints:
# The dir function to get all entries of a module
#
# The inspect.isfunction function can be used to test if given object is a function
#
# x.__doc__ gives the docstring for x.
#
# The __import__ function can be used to import a module by name


def my_doc(name):
    from inspect import isfunction
    p = __import__(name)
    print('Help on module', name, '\n\nDESCRIPTION\n')
    print(p.__doc__)

    print('\nFUNCTIONS\n')

    for i in dir(__import__(name)):
        if isfunction(p.__getattribute__(i)):
            print(i + '()')


def my_doc1(name):
    from inspect import getmembers, isfunction
    p = __import__(name)
    print('Help on module', name, '\n\nDESCRIPTION\n')
    print(p.__doc__)

    print('\nFUNCTIONS\n')

    for f in getmembers(p, predicate=lambda x: isfunction(x)):
        print(f[0]+'()')


if __name__ == '__main__':
    my_doc('os')
