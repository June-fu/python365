#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2021-05-03 00:36:49
 # @ Modified by: june-fu
 # @ Modified time: 2021-05-03 00:36:57
 # @ Description:Write a Pandas program to convert DataFrame column type from string to datetime
 '''


import pandas as pd
import numpy as np
s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])
print("String Date:\n", s)

df = pd.DataFrame(pd.to_datetime(s))
print(df)