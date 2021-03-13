#!/usr/bin/pyton
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-13 23:17:28
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-13 23:17:31
 # @ Description:
the read_fwf() function works with data files that have known and fixed column widths.
 '''

import pandas as pd

#  a typical fixed-width data file "bar.csv"
colspecs = [(0, 6), (8, 20), (21, 33), (34, 43)]
df = pd.read_fwf("./data/bar.csv", colspecs=colspecs, header=None, index_col=0)
print(df)

# # Widths are a list of integers
widths = [6, 14, 13, 10]
df2 = pd.read_fwf("./data/bar.csv", widths=widths, header=None)
print(df2)

# read_fwf supports the dtype parameter for specifying the types of parsed columns to be different from the inferred type.
print(df.dtypes)
print(pd.read_fwf("./data/bar.csv",header=None, dtype={2: 'object'}).dtypes)