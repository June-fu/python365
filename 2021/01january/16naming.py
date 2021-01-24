#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-24 22:38:11
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-24 22:39:32
 # @ Description:
 '''

import pandas as pd
from io import StringIO

data = ('a,b,c\n'
         '1,2,3\n'
         '4,5,6\n'
         '7,8,9')
print(pd.read_csv(StringIO(data)))

# By specifying the names argument in conjunction with header you can indicate other names to use and whether or not to throw away the header row 
print(pd.read_csv(StringIO(data), names=['foo', 'bar', 'baz'], header=0))
print(pd.read_csv(StringIO(data), names=['foo', 'bar', 'baz'], header=None))

# If the header is in a row other than the first, pass the row number to header. This will skip the preceding rows:
data2 = ('skip this skip it\n'
         'a,b,c\n'
         '1,2,3\n'
         '4,5,6\n'
         '7,8,9')
print(pd.read_csv(StringIO(data2), header=1))