#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/9
"""
现在有3只怪兽，他们的都有自己的血量a,b,c(1<=a,b,c<=100)，当Tom打死第一怪兽的时候花费的代价为0，
其余的怪兽的代价为当前的怪兽的血量减去上一个怪兽的血量的绝对值。问Tom打死这些怪兽所需要的最小代价
input:分别输入三只怪兽的血量
output:输出打死三只怪兽的最小代价
"""


def fight_monster():
    health_lst = []
    for i in range(3):
        health_lst.append(input('Please enter the health of the three monsters:'))

    lst = [(int(i), int(j), int(k)) for i in health_lst for j in health_lst for k in health_lst
           if i != j and j != k and i != k]
    cost_lst = {}
    min_cost = float('inf')  # 正无穷大
    for t in lst:
        cost = 0
        for i in range(len(t)):
            if i > 0:
                import math
                cost += math.fabs(t[i] - t[i-1])
        if cost < min_cost:
            cost_lst.clear()
            min_cost = cost
            cost_lst[t] = cost
        elif cost == min_cost:
            cost_lst[t] = cost
    print(cost_lst)


if __name__ == '__main__':
    fight_monster()
