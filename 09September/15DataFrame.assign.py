#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/23
"""
Assigning new columns in method chains
assign() method that allows you to easily create new columns that are potentially derived from existing columns.
assign always returns a copy of the data, leaving the original DataFrame untouched.
"""
import pandas as pd

iris = pd.read_csv('../data/iris.csv')
print(iris.head())

iris2 = iris.assign(sepal_ratio=iris['SepalWidth'] / iris['SepalLength'])
print(iris2.head())

# We can also pass in a function of one argument to be evaluated on the DataFrame being assigned to
iris3 = iris.assign(sepal_ratio=lambda x: (x['SepalWidth'] / x['SepalLength']))
print(iris3.head())

iris4 = iris.assign(sepal_ratio=lambda x: (x.SepalWidth / x.SepalLength))
print('iris4:\n', iris4.head())

iris.query('SepalLength > 5').assign(SepalRatio=lambda x: x['SepalWidth'] / x['SepalLength'],
                                     PetalRatio=lambda x: x['PetalWidth'] / x['PetalLength']) \
    .plot(kind='scatter', x='SepalRatio', y='PetalRatio')
