#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/11
"""
合并两个字典
"""


# 在相交的情况下，使用第二个字典中的值
def combine_dict(dict1, dict2):
    return {**dict1, **dict2}


if __name__ == '__main__':
    dict_1 = {'apple': 9, 'banana': 6}
    dict_2 = {'banana': 4, 'orange': 8}

    print(combine_dict(dict_1, dict_2))
