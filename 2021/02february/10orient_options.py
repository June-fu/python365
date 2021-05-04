#!/usr/bin/local
'''
 # @ Author: june-fu
 # @ Create Time: 2021-05-04 22:54:25
 # @ Modified by: june-fu
 # @ Modified time: 2021-05-04 22:54:27
 # @ Description:
 '''

import pandas as pd

dfjo = pd.DataFrame(dict(A=range(1, 4), B=range(4, 7), C=range(7, 10)),
                    columns=list('ABC'), index=list('xyz'))
print(dfjo)

sjo = pd.Series(dict(x=15, y=16, z=17), name='D')
print(sjo)

# column oriented(default for DataFrame)
print(dfjo.to_json(orient='columns'))

# index oriented(default for series)
print(dfjo.to_json(orient='index'))
print(sjo.to_json())

# record oriented
# serializes the data to a JSON array of column -> value records, index labels are not included
print(dfjo.to_json(orient='records'))
print(sjo.to_json(orient='records'))

# value oriented
print(dfjo.to_json(orient='values'))

# Split oriented 
# serializes to a JSON object containing separate entries for values, index and columns.
print(dfjo.to_json(orient='split'))
print(sjo.to_json(orient='split'))

# Table oriented
print(dfjo.to_json(orient='table'))
print(sjo.to_json(orient='table'))