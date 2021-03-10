#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-10 22:02:23
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-10 22:02:26
 # @ Description:
Handling “bad” lines
 '''
import pandas  as pd
from io import StringIO

data = (
    'a,b,c\n'
    '1,2,3\n'
    '4,5,6,7\n' # malformed lines
    '8,9,10'
)

# Lines with too many fields will raise an error by default
# df = pd.read_csv(StringIO(data))
# print(df)

# you can elect to skip bad lines
print(pd.read_csv(StringIO(data), error_bad_lines=False))

# you can also use usecols parameter to eliminate extraneous column data
print(pd.read_csv(StringIO(data), usecols=[0, 1, 2]))