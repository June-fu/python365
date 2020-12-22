#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-10 23:13:53
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-10 23:14:29
 # @ Description:
 applymap() on DataFrame, map() on Series accept any python function taking a single value and returning a single value
 '''

import pandas as pd
import numpy as np

df4 = pd.DataFrame(np.random.randn(4, 3), columns=['one', 'two', 'three'],
                    index=['a', 'b', 'c', 'd'])
print(df4)

def f(x):
    return len(str(x))

print(df4['one'].map(f))
print(df4.applymap(f))

# Series.map() can be used to easily "map" values defined by a second Series
s = pd.Series(['six', 'seven', 'six', 'seven', 'six'], index=['a', 'b', 'c', 'd', 'e'])
t = pd.Series({"six": 6., "seven": 7.})

print(s.map(t))