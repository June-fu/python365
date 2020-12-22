#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-21 12:52:39
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-21 12:52:43
 # @ Description:using yield to create a simple iterator
 '''
def foo(lst):
    for x in lst:
        yield x
        yield x*2

a = [1, 3]
print(foo(a))
print(list(foo(a)))