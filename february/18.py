#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/15
"""
1、输入一个奇数，然后判断最少几个 9 除于该数的结果为整数
2、代码实现每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换第二位和第三位交换
"""


def odd_nine(odd):
    s = 1
    num = 9
    while num % odd:
        num = num * 10 + 9
        s += 1
    return s, num


# 代码实现每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换第二位和第三位交换
def num_change(n):
    lst1 = str(n)
    lst = []
    for i in range(len(lst1)):
        lst.append((int(lst1[i]) + 5) % 10)

    lst[-1], lst[-2], lst[-3], lst[-4] = lst[-4], lst[-3], lst[-2], lst[-1]
    return ''.join(str(x) for x in lst)


# 第一位置换后需要乘以1，第二位乘以10，第三位乘以100,第四位乘以1000——pow(10, i)
def num_change1(n):
    lst1 = str(n)
    total = 0
    for i in range(len(lst1)):
        total += ((int(lst1[i]) + 5) % 10) * pow(10, i)
    return total


if __name__ == '__main__':
    x = input('please input a odd number:')
    s1, r = odd_nine(int(x))
    print(f'{s1}个 9 可以被{x}整除:{r}')

    print(num_change(1234))
    print(num_change1(1234))
