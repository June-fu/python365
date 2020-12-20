#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-20 20:57:17
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-20 20:57:26
 # @ Description:
display a summary of the basic information about a specified DataFrame and its data
'''
import pandas as pd
import numpy as np

dct1 = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(dct1)

df = pd.DataFrame(data=dct1, index=labels)
print("Summary of the basic information about this DataFrame and its data:\n", df.info())