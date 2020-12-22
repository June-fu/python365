#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-11 22:59:48
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-11 22:59:50
 # @ Description:Reindexing to align with another objects

 '''
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4, 3), columns=['one', 'two', 'three'],
                index=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
print(df2)

df3 = pd.DataFrame(np.random.randn(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
print(df.reindex_like(df2))

print(df3.reindex_like(df))