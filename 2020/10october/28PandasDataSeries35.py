#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-14 22:37:27
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-14 22:37:31
 # @ Description:
Write a Pandas program to create a TimeSeries to display all the Sundays of given year
'''

import pandas as pd
import numpy as np

s = pd.Series(pd.date_range('2020-01-01', periods=52, freq='W-SUN'))
print("All Sundays of 2020:\n", s)