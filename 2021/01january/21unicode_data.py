#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-20 22:32:08
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-20 22:32:14
 # @ Description:
the encoding argument should be used for encoded unicode data, 
which will result in byte strings being decoded to unicide in the result
 '''

import pandas as pd
from io import BytesIO

data = (b'word,length\n'
         b'Tr\xc3\xa4umen,7\n'
         b'Gr\xc3\xbc\xc3\x9fe,5')
data = data.decode('utf-8').encode('latin-1')
df = pd.read_csv(BytesIO(data), encoding='latin-1')

print(df)
print(df['word'][1])