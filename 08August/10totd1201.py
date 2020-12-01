#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-01 23:17:23
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-01 23:17:27
 # @ Description:
 Dictionary Merge
'''
p1 = {"X": 100, "Y": 200, "Z": 300}
p2 = {"A": 10, "B": 20, "C": 30}

p3 = {**p1, **p2}
print(p3)