# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/29
"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

"""


def how_many_numbers():
    total_numbers = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                    if i != j and j != k and k != i:
                        total_numbers += 1
                        print(i * 100 + j * 10 + k)
    return total_numbers


if __name__ == '__main__':
    x = how_many_numbers()
    print("1、2、3、4，能组成{}个互不相同且无重复数字的三位数".format(x))
