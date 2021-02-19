#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-19 22:25:42
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-19 22:25:46
 # @ Description:
 the parameter header uses row numbers (ignoring commented/empty lines),
  while skiprows uses line numbers (including commented/empty lines):
 '''

import pandas as pd
from io import StringIO

data = ('#comment\n'
         'a,b,c\n'
         'A,B,C\n'
         '1,2,3')
# header parameter (ignoring commented/empty lines)
print(pd.read_csv(StringIO(data), comment='#', header=1))

# skiprows parameter (including commented/empty lines)
print(pd.read_csv(StringIO(data), comment='#', skiprows=1))

# if both header and skiprows are specified, header will be relative to the end of skiprows
data2 = ('# empty\n'
        '# second empty line\n'
        '# third emptyline\n'
        'X,Y,Z\n'
        '1,2,3\n'
        'A,B,C\n'
        '1,2.,4.\n'
        '5.,NaN,10.0\n')
print(pd.read_csv(StringIO(data2), comment='#', header=1, skiprows=4))