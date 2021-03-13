#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-13 22:56:10
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-13 22:56:12
 # @ Description:
 Quotes (and other escape characters) in embedded fields can be handled in any number of ways.
  One way is to use backslashes; to properly parse this data, you should pass the escapechar option:
 '''
import pandas as pd
from io import StringIO

data = 'a,b\n"hello, \\"Bob\\", nice to see you",5'
print(data)
print(pd.read_csv(StringIO(data), escapechar='\\'))