#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-20 21:47:45
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-21 22:07:54
 # @ Description:
Write a Pandas program to sort the DataFrame first by 'name' in descending order, 
then by 'score' in ascending order.
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

df.sort_values(by=['name', 'score'], ascending=[False, True])
print("Sort the DataFrame:\n", df)