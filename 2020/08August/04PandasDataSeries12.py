#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-24 22:11:22
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-24 22:11:24
 # @ Description:
Write a Pandas program to add some data to an existing Series.
 '''
import pandas as pd
import numpy as np

s = pd.Series(['100', '200', 'python', '300.12', '400'])
print('Original Series:\n', s)

print('Data Series after adding some data:\n', s.append(pd.Series(['500', 'php'])))
