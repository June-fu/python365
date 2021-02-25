#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-25 22:25:00
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-25 22:25:03
 # @ Description:
Parsing a CSV with mixed timezones
 '''

import pandas as pd
from io import StringIO

content = """
a
2000-01-01T00:00:00+05:00
2000-01-01T00:00:00+06:00"""
df = pd.read_csv(StringIO(content), parse_dates=['a'])
print(df['a'])

# to parse the mixed_timezone values as a datetime column ,pass a partially-applied 
# to_datetime() with utc=True as the date_parser
df2 = pd.read_csv(StringIO(content), parse_dates=['a'],
        date_parser=lambda col: pd.to_datetime(col, utc=True))
print(df2['a'])