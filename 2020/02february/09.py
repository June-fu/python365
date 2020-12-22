#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/7
"""
模仿静态变量(static)演示一个python作用域使用方法
Knowledge:
    Python 使用 LEGB 的顺序来查找一个符号对应的对象:locals -> enclosing function -> globals -> builtins
"""


# 学习使用auto定义变量的用法。
def auto_func():
    var = 1
    print('The var in auto_func is {}'.format(var))
    var += 1


class StaticVar:
    var = 5

    def inc(self):
        self.var += 1
        print('The var in the StaticVar is {}'.format(self.var))


class StaticVar2:

    def inc(self):
        global var
        var += 1
        print('The var in the StaticVar2 is {}'.format(var))


if __name__ == '__main__':
    var = 2
    sv = StaticVar()
    sv2 = StaticVar2()
    for i in range(3):
        var += 1
        print('the local var is {}'.format(var))
        auto_func()
        sv.inc()
        sv2.inc()





