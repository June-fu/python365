#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-26 23:49:52
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-26 23:49:59
 # @ Description:Using list comprehensions to shorten for loops
 '''
x = [1, 2, 3, 4, 5]
result = []
for idx in range(len(x)):
    result.append(x[idx] * 2)

print(result)

# list comprehensions
print([(element * 2) for element in x])
