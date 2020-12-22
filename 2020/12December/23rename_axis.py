#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-20 20:36:03
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-20 20:36:10
 # @ Description:
 rename_axis() allow specific names of a Multiindex to be changed(as opposed to the labels)
 '''

import pandas as pd


df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6],
                    'y': [10, 20, 30, 40, 50, 60]},
                    index=pd.MultiIndex.from_product([['a', 'b', 'c'], [1, 2]],
                    names=['let', 'num']))

print(df)
print(df.rename_axis(index={'let': 'abc'}))
print(df.rename_axis(index=str.upper))    