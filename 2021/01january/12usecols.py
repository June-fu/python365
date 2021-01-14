#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-14 23:35:50
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-14 23:35:53
 # @ Description:
 '''

import  pandas as pd
from io import StringIO

data = ('col1,col2,col3\n''a,b,1\n''a,b,2\n''c,d,3')
print(pd.read_csv(StringIO(data)))

#If callable, the callable function will be evaluated against the column names, 
# returning names where the callable function evaluates to True:
print(pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['COL1', 'COL3']))
# Using this parameter results in much faster parsing time and lower memory usage.