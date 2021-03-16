#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-16 22:31:12
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-16 22:31:17
 # @ Description:
 '''

import pandas as pd

data = pd.read_csv('./data/tmp.csv', sep='|')
print(data)

# by specifying a chunksize to read_csv ,the return value will be an iterable object of type TextFileReader
reader = pd.read_csv('./data/tmp.csv', sep='|', chunksize=4)
print(type(reader))

for chunk in reader:
    print(chunk)

# specifying iterator = True will also return the TextFileReader object
reader2 = pd.read_csv('./data/tmp.csv', sep='|', iterator=True)
print(reader2.get_chunk(5))