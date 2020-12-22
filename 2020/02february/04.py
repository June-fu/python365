#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/3
"""
bounce()一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
import random


def bounce(num):
    height = 100
    total = 0
    for i in range(num):
        total += height
        height /= 2
    return total, height


# 猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# 逆向思维推论问题
def peach():
    total = 1
    for i in range(1, 10):
        total = (total + 1) * 2
    return total


# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，编程序找出三队赛手的名单。
def game():
    m = ['a', 'b', 'c']
    n = ['x', 'y', 'z']
    # 互不相同的不同组合
    lst = [(i, j, k) for i in n for j in n for k in n if i != j and j != k and i != k]
    lst1 = []
    for s in range(len(lst)):
        lst1.append([(o, p) for o, p in zip(m, lst[s])])  # 不同组合的列表

    for t in lst1:
        if not ((('a', 'x') in t) or (('c', 'x') in t) or (('c', 'z') in t)):
            # 不能使用lst1.remove(t),这样就修改了lst1
            print(t)


# 列表表达式一句实现
def game2():
    return [(i, j, k) for i in ['x', 'y', 'z'] for j in ['x', 'y', 'z'] for k in ['x', 'y', 'z']
            if i != j and j != k and i != k and i != 'x' and k not in ('x', 'z')]


if __name__ == '__main__':
    t, h = bounce(10)
    print("它在第10次落地时，共经过{}米,第10次反弹高度是{}米".format(t, h))

    print(peach())
    game()

    w = [(i, j, k) for i in ['x', 'y', 'z'] for j in ['x', 'y', 'z'] for k in ['x', 'y', 'z']
         if i != j and j != k and i != k and i != 'x' and k not in ('x', 'z')]
    print('order is a -- %s\t b -- %s\tc--%s' % w[0])
