#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-10 23:45:16
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-10 23:45:27
 # @ Description:
  to_numeric() provides another argument downcast, which gives the option of downcasting the newly (or already) numeric data to a smaller dtype,
   which can conserve memory:
 '''

import pandas as pd

m = ['1', '2', '3']
print(pd.to_numeric(m, downcast='integer')) # smallest signed int dtype
print(pd.to_numeric(m, downcast='signed'))# same as integer
print(pd.to_numeric(m, downcast='unsigned')) # smallest unsigned int dtype
print(pd.to_numeric(m, downcast='float'))# smallest float dtype