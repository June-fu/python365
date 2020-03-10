#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/11
"""
What will be the output of the following program?
"""


# Inheritance
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'


class B(A):
    def g(self):
        return 'B'


def f():
    try:
        print("a")
        return
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")


if __name__ == '__main__':
    a = A()
    b = B()
    print(a.f(), b.f())
    print(a.g(), b.g())

    # Errors and Exceptions
    try:
        print("a")
    except:
        print('b')
    else:
        print("c")
    finally:
        print("d")
    # acd

    try:
        print("a")
        raise Exception("doom")
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")
    # abd

    f()
    # ad
