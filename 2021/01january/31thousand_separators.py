#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-28 22:27:54
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-28 22:27:58
 # @ Description:
 '''

import pandas as pd
from io import StringIO

data = """ID|level|category
Patient1|123,000|x
Patient2|23,000|y
Patient3|1,234,018|z"""
df = pd.read_csv(StringIO(data), sep='|')
print(df)
print(df.level.dtype)

# the thousand keyword allows integers to be parsed correctly
df2 = pd.read_csv(StringIO(data), sep='|', thousands=',')
print(df2)
print(df2.level.dtype)