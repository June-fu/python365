#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-18 23:31:26
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-18 23:31:28
 # @ Description:
 Categorical columns can be parsed directly 
 by specifying dtype='category' or dtype=CategoricalDtype(categories, ordered).
 '''

import pandas as pd
from io import StringIO

data = ('col1,col2,col3\n'
        'a,b,1\n'
        'a,b,2\n'
        'c,d,3')
print(pd.read_csv(StringIO(data)))
print(pd.read_csv(StringIO(data)).dtypes)
print(pd.read_csv(StringIO(data), dtype='category').dtypes)

#Individual columns can be parsed as a Categorical using a dict specification:
print(pd.read_csv(StringIO(data), dtype={'col1': 'category'}).dtypes)