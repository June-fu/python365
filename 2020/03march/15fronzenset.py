#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-24 22:59:21
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-24 22:59:24
 # @ Description:
frozenset() function allows lists to be immutable
 '''

lst = ['January', 'march', 'April']
f_lst = frozenset(lst)
print(f_lst)

# f_lst[0] = 'aa' 
# this will rasie a TypeError