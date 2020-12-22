#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-22 23:22:36
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-22 23:22:41
 # @ Description:
 Write a Pandas program to insert a new column in existing DataFrame
 '''

import pandas as pd
import numpy as np

dct1 = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=dct1, index=labels)
print(df)

color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']
df['color'] = color
print(df)