#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-23 23:03:22
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-23 23:03:23
 # @ Description:
 You can specify a list of column lists to parse_dates
 '''

import pandas as pd
from io import StringIO

data =('KORD,19990127, 19:00:00, 18:56:00, 0.8100\n'
        'KORD,19990127, 20:00:00, 19:56:00, 0.0100\n'
        'KORD,19990127, 21:00:00, 20:56:00, -0.5900\n'
        'KORD,19990127, 21:00:00, 21:18:00, -0.9900\n'
        'KORD,19990127, 22:00:00, 21:56:00, -0.5900\n'
        'KORD,19990127, 23:00:00, 22:56:00, -0.5900')

# You can specify a list of column lists to parse_dates
df = pd.read_csv(StringIO(data), header=None, parse_dates=[[1, 2], [1, 3]])
print(df)


# you can choose to retain the component date columns via keep_date_col keyword
df2 = pd.read_csv(StringIO(data), header=None, parse_dates=[[1, 2], [1, 3]], keep_date_col=True)
print(df2)

# you can also use a dict to specify custom name columns
date_spec = {'nominal': [1, 2], 'actual': [1, 3]}
df3 = pd.read_csv(StringIO(data), header=None, parse_dates=date_spec)

print(df3)