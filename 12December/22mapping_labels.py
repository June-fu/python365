#！/usr/local/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-20 19:28:28
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-20 19:28:32
 # @ Description:
Renaming or mapping labels
 '''
import pandas as pd
import numpy as np

s = pd.Series(np.random.rand(5), index=['a', 'b', 'c', 'd','e'])
print(s)

# the raname() method allows you to relabel an axis based on some mapping(a dict or Series) or an arbitrary function
print(s.rename(str.upper))

df = pd.DataFrame(np.random.randn(4, 3), columns=['one', 'two', 'three'],
                index=['a', 'b', 'c', 'd'])
print(df)

print(df.rename(columns={'one': 'foo', 'two': 'bar'},
                index={'a': 'apple', 'b': 'banana', 'd': 'durian'}))

# DF also supports an "axis-style" call convention
print(df.rename({'one': 'foo', 'two': 'bar'}, axis='columns'))
print(df.rename({'a': 'apple', 'b': 'banana', 'd': 'durian'}, axis='index'))

# Finally, rename() also accepts a scalar or list-like for altering the Series.name attribute.
print("Series.name:\n", s.rename('scalar-name'))

