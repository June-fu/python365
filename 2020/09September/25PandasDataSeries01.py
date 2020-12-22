#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-19 22:35:34
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-19 22:35:51
 # @ Description:
 Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module
 '''

import pandas as pd
import numpy as np

array1 = np.arange(10)
print(array1)
s = pd.Series(array1)
print(s)