#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-24 22:59:30
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-24 22:59:32
 # @ Description:
 you can specify a date_parser function to take full advantage of the flexibility of the date parsing API
 '''

import pandas as pd
from io import StringIO

data =('KORD,19990127, 19:00:00, 18:56:00, 0.8100\n'
        'KORD,19990127, 20:00:00, 19:56:00, 0.0100\n'
        'KORD,19990127, 21:00:00, 20:56:00, -0.5900\n'
        'KORD,19990127, 21:00:00, 21:18:00, -0.9900\n'
        'KORD,19990127, 22:00:00, 21:56:00, -0.5900\n'
        'KORD,19990127, 23:00:00, 22:56:00, -0.5900')
date_spec = {'nominal': [1, 2], 'actual': [1, 3]}
df = pd.read_csv(StringIO(data), header=None, parse_dates=date_spec,
                date_parser=pd.io.date_converters.parse_date_time)
print(df)