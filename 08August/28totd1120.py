#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-20 23:31:07
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-20 23:31:12
 # @ Description: Creating decorator to separate concerns
'''

from functools import wraps

def add_sandwich(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs) + ' sandwich'
    return wrapper

@add_sandwich
def ham():
    return 'ham'

print(ham())

