#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-27 23:32:37
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-27 23:32:42
 # @ Description:Summarizing data
 there is a convenient describe() function which computes a variety of summary statistics about
 a Series or the columns of a DataFrame(excluding NAs of course)
 '''
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(1000))
s[::2] = np.nan

print(s.describe())

df = pd.DataFrame(np.random.randn(1000, 5),
                columns=['a', 'b', 'c', 'd', 'e'])
df.iloc[::2] = np.nan
print(df.describe())

# you can select specific percentiles to include in the ouput
print(s.describe(percentiles=[.05, .25, .75, .95]))

# for a non-number Series object
s2 = pd.Series(['a', 'a', 'b', 'b', 'a', 'a', np.nan, 'c', 'd', 'a'])
print(s2.describe())

# on mixed-type DataFrame object, describe() will restrict the summary to include only numerical columns
df = pd.DataFrame({
    'a': ['Yes', 'Yes', 'No', 'No'],
    'b': range(4)
})

print(df.describe())

# this behavior can be controlled by providing a list of types as include/exclude arguments.
print(df.describe(include=['object']))
print(df.describe(include=['number']))
print(df.describe(include='all'))