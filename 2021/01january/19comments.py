#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-19 21:55:21
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-19 21:55:25
 # @ Description: comment parameter
 if the comment parameter is specified, then completely commented lines will be ignord.
 '''
import pandas as pd
import numpy as np
from io import StringIO

data = ('\n'
        'a,b,c\n'
        '  \n'
        '# commented line\n'
        '1,2,3\n'
        '\n'
        '4,5,6')

print(data)

# comment parameter is specified
print(pd.read_csv(StringIO(data), comment='#'))

# if skip_blank_lines=False, then read_csv will not ignore blank lines
data2 = ('a,b,c\n'
         '\n'
         '1,2,3\n'
         '\n'
         '\n'
         '4,5,6')
print(pd.read_csv(StringIO(data2), skip_blank_lines=False))