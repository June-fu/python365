#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-29 23:32:01
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-29 23:32:08
 # @ Description:
 Continuous values can be descretized using the cut() and qcut() functions
 '''
import pandas as pd
import numpy as np

arr = np.random.randn(20)
factor = pd.cut(arr, 4)

print(factor)
print(pd.cut(arr, [-5, -1, 0, 1, 5]))

# qcut() computes sample quantiles
arr2 = np.random.randn(30)
factor2 = pd.qcut(arr, [0, .25, .5, .75, 1])
print(factor2)
print(pd.value_counts(factor2))

# We can alse pass infinite values to difine the bins
factor3 = pd.cut(arr, [-np.inf, 0, np.inf])
print(factor3)
