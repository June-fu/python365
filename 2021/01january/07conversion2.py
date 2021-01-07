#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-07 23:49:08
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-07 23:49:13
 # @ Description:
 To force a conversion, we can pass in an errors argument, which specifies how pandas should deal with elements that cannot be converted to desired dtype or object.
 '''

import pandas as pd
import datetime

m = ['apple', datetime.datetime(2021, 3, 2)]
# By default, errors='raise', meaning that any errors encountered will be raised during the conversion process
# if errors='coerce' these errors will be ignored and 
# pandas will convert problematic elements to pd.NaT (for datetime and timedelta) or np.nan (for numeric)
print(pd.to_datetime(m, errors='coerce'))
# errors='ignore'  which will simply return the passed in data if it encounters any errors with the conversion to a desired data type:
print(pd.to_datetime(m, errors='ignore'))

m = ['apple', 2, 3]
print(pd.to_numeric(m, errors='coerce'))
# errors='ignore'
print(pd.to_numeric(m, errors='ignore'))

m = ['apple', pd.Timedelta('1day')]
print(pd.to_timedelta(m, errors='coerce'))

# errors='ignore'  which will simply return the passed in data if it encounters any errors with the conversion to a desired data type:
