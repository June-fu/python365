#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-08 00:10:22
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-08 00:10:25
 # @ Description:
Using the squeeze keyword, the parser will return output with a single column as a Series:
 '''

import pandas as pd
from io import StringIO

data = ('level\n'
        'Patient1,123000\n'
        'Patient2,23000\n'
        'Patient3,1234018\n')

output = pd.read_csv(StringIO(data), squeeze=True)
print(output)
print(type(output))