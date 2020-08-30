#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/8/30
"""
1、如何引入pandas并查看版本
2、学习series以及怎么通过其他数据类型转换成Series
"""

import pandas as pd
import numpy as np

print(pd.__version__)
print(pd.show_versions(as_json=True))

my_list = list('abcdefghijklmnopqrstuvwxyz')
my_array = np.arange(26)
my_dict = dict(zip(my_list, my_array))

series1 = pd.Series(my_list)
series2 = pd.Series(my_array)
series3 = pd.Series(my_dict)

print(series3.head(10))
print(series3)
