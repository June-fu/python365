#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-08 22:59:13
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-08 22:59:15
 # @ Description:
 The common values True, False, TRUE, and FALSE are all recognized as boolean. 
 true_value() and false_value() options
 '''

import pandas as pd
from io import StringIO

data = ('a,b,c\n'
        '1,Yes,2\n'
        '3,No,4')

print(pd.read_csv(StringIO(data)))

df = pd.read_csv(StringIO(data), true_values=['Yes'], false_values=['No'])
print(df)