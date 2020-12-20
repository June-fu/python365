#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-20 18:04:50
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-20 18:05:06
 # @ Description:
Dropping labels from an axis
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4, 3), columns=['one', 'two', 'three'],
                index=['a', 'b', 'c', 'd'])
print(df)

# drop() function removes a set of labels from an axis
print(df.drop(['a', 'd'], axis=0))
print(df.drop(['one'], axis=1))

# note that if the axis is not defined, it also works ,but is a bit less obvious/clean：
print(df.drop(['a', 'd']))