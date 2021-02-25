#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-25 22:31:47
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-25 22:31:53
 # @ Description:Inferring datetime format
 '''

import pandas as pd
from io import StringIO

data =('date,A,B,C\n'
'20090101,a,1,2\n'
'20090102,b,3,4\n'
'20090103,c,4,5')

# try to infer the format for the index column 
df = pd.read_csv(StringIO(data), index_col=0, parse_dates=True, infer_datetime_format=True)
print(df)
