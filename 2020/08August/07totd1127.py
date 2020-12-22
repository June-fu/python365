#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-27 22:07:00
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-27 22:07:42
 # @ Description:
Inserting if statements using conditional list comprehensions
 '''

import pandas as pd

x = [1, 2, 3, 4, 5, 6]
result = []
for idx in range(len(x)):
    if x[idx] % 2 == 0:
        result.append(x[idx] * 2)
    else:
        result.append(x[idx])
print(result)

# using conditional list comprehensions
print([(element * 2 if element % 2 == 0 else element) for element in x])