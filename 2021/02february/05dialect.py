#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-13 22:45:08
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-13 22:45:10
 # @ Description:
 '''

import pandas as pd
from io import StringIO

data = 'label1,label2,label3\nindex1,"a,c,e\nindex2,b,d,f'
print(data)

# By default, read_csv uses the Excel dialect and treats the double quote as the quote character
import csv 
dia = csv.excel()

dia.quoting = csv.QUOTE_NONE

df = pd.read_csv(StringIO(data), dialect=dia)
print(df)

# all of the dialect options can be specified separately by keyword arguments
data2 = 'a,b,c~1,2,3~4,5,6'
print(pd.read_csv(StringIO(data2), lineterminator='~'))

# another common dialect option is skipinintialspace ,to skip any whitespace after a delimiter
data3 = 'a, b, c\n1, 3, 2\n4, 5, 6'
print(data3)
print(pd.read_csv(StringIO(data3), skipinitialspace=True))