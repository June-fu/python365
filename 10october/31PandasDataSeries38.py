#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-17 23:06:46
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-17 23:19:56
 # @ Description:
 Write a Pandas program to check the equality of two given series
 '''

import pandas as pd

nums1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original Series:\n", nums1, nums2)
print("check 2 series are equal or not?\n", nums1 == nums2)