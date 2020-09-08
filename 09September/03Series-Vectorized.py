#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/9
"""
Vectorized operations and label alignment with Series
使用Pandas的Series与使用numpy中的原始数组一样，通常不需要逐值循环；
Series可以传递给大多数需要ndarray的Numpy方法
"""
import numpy as np
import pandas as pd

s = pd.Series(data=np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

print(s + s)
print(s * 2)
# 计算指数
print(np.exp(s))

