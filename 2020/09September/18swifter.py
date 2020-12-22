#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/18
"""
利用swifter对apply函数加速
由于apply只是将一个函数应用到数据帧的每一行，调用单个处理器；如何并行化处理，利用多核能力？
swifter这样做：
1、检查你的函数是否可以向量化，如果可以，就使用向量化计算。
2、如果无法进行向量化，swifter会自动决定哪一个最快：使用Dask进行并行处理还是只使用pandas apply。
"""
import pandas as pd
import swifter

df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [5, 6, 7, 8]})
print(df)

# runs on single core
df['x2'] = df['x'].apply(lambda x: x**2)
# runs on multiple cores
df['x3'] = df['x'].swifter.apply(lambda x: x**2)

print(df)
# use swifter apply on whole dataframe
# axis = 0 or 'index': apply function to each column.
# axis = 1 or 'columns': apply function to each row.
df['agg'] = df.swifter.apply(lambda x: x.sum() - x.min(), axis=1)
print(df)

