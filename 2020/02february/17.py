#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/15
"""
8进制转换为10进制
方法一，正向思考
方法二，逆向思考
例：将十进制数115转化为八进制数
115 % 8…… 3
14 % 8…… 6
1 % 8…… 1
（115）10 = （163）8
"""


def octal_decimal(octal):
    decimal = 0
    for i in range(len(octal)):
        decimal += int(octal[i]) * pow(8, len(octal) - 1 - i)
    return decimal


# 逆向思考，10进制转换8进制的时候，用的是求余数
def octal_decimal2(octal):
    n = 0
    for i in range(len(octal)):
        n = n * 8 + int(octal[i])
        print(n)
    return n


# 求0—7所能组成的奇数个数
def odd():
    total = 4
    s = 4  # 一位数有4个
    for i in range(2, 9):

        if i == 2:  # 两位数有 7*4 个
            s *= 7
        else:
            s *= 8  # 三到八位数有7*8...*4个
        total += s
        print(i, s)
    return total


if __name__ == '__main__':
    # oct = input("please input a octal number:")
    # print(octal_decimal(oct))
    # print(octal_decimal2(oct))

    print(odd())

