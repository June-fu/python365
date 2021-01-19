#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-19 21:27:22
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-19 21:27:25
 # @ Description:
 '''

import pandas as pd
from io import StringIO
from pandas.api.types import CategoricalDtype

data = ('col1,col2,col3\n'
        'a,b,1\n'
        'a,b,2\n'
        'c,d,3')
dtype = CategoricalDtype(['d', 'c', 'b', 'a'], ordered=True)
print(pd.read_csv(StringIO(data), dtype={'col1': dtype}).dtypes)

# when using dtype=CategoricalDtype ,"unexcepected" values outsides of dtype.categories 
# are treated as missing values;
# This matches the behavior of Categorical.set_categories().
dtype = CategoricalDtype(['a', 'b', 'd'])
print(pd.read_csv(StringIO(data), dtype={'col1': dtype}).col1)

df = pd.read_csv(StringIO(data), dtype='category')
print(df['col3'])

df['col3'].cat.categories = pd.to_numeric(df['col3'].cat.categories)
print(df['col3'])