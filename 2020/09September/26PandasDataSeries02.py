#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-20 23:22:57
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-20 23:23:25
 # @ Description:
 # 2.Write a Pandas program to convert a Panda module Series to Python list and it's type
 '''

import pandas as pd
import numpy as np

s = pd.Series(np.arange(10))
print(s)

list1= s.to_list()
print(list1)
print(type(list1))