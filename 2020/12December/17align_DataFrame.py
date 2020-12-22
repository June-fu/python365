#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-14 22:15:14
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-14 22:15:17
 # @ Description:
 '''
import pandas as pd
import numpy as np

# For DataFrames, the join method will be applied to both the index and the columns by default
df = pd.DataFrame(np.random.randn(4,3), index=['a', 'b', 'c', 'd'],
                columns=['one', 'two', 'three'])

df1 = pd.DataFrame(np.random.randn(3,2), index=['a', 'b', 'c'],
                columns=['one', 'two'])
print(df.align(df1, join='inner'))

# You can also pass an axis option to only align on the specified axis:
print(df.align(df1, join="inner", axis=0))

# if you pass a series to DataFrame.align(), you can choose to align both objects
# either on the DataFrame's index or columns using the axis argument
print(df.align(df1.iloc[0], axis=1))