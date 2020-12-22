#!/usr/local/bin/pyton
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-29 22:56:27
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-29 22:56:38
 # @ Description:
Simplify the way you collapse nested lists
 '''
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(x)

# method 1
result = []
for sublist in x:
    for item in sublist:
        result.append(item)
print(result)

# method 2
print([item for sublist in x for item in sublist])

# method 3
import itertools
print(list(itertools.chain(*x)))