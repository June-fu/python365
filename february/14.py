#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/11
"""
有n个人围成一圈，顺序排号。从第一个人开始报数，凡报到3的人退出圈子，问最后留下的是原来第几号的那位
"""


# 向后移M个数字
def move_backward(m):
    a = [2, 8, 6, 1, 78, 45, 34, 2]
    for i in range(len(a) - m):
        a.append(a[0])
        a.pop(0)
    return a


def report(num):
    lst = []
    for i in range(num):
        lst.append(i + 1)

    t = 0
    while len(lst) > 1:
        for x in range(3):
            t += 1
            if x == 2:
                t -= 1
                lst.pop(t)
            if t == len(lst):
                t = 0
    return lst[0]


if __name__ == '__main__':
    print(move_backward(5))
    print(report(34))
