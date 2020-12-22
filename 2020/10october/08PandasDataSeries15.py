#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-27 21:52:28
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-27 21:53:12
 # @ Description:
 Write a Pandas program to create the mean and standard deviation of the data of a given Series
 '''

import pandas as pd
import numpy as np

s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print("Original Data Series:\n", s)
print("Mean of the said Data Series:\n", s.mean())
print("Standard deviation of the said Data Series:\n", s.std())