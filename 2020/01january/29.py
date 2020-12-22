#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/1
"""
Problem 24: Provide an implementation for zip function using list comprehensions.
input:  zip1([1, 2, 3], ["a", "b", "c"])
[(1, "a"), (2, "b"), (3, "c")]
"""
# https://lerner.co.il/2016/08/30/implementing-zip-list-comprehensions/
# https://djangostars.com/blog/list-comprehensions-and-generator-expressions/?utm_campaign=CodeTengu&utm_medium=web&utm_source=CodeTengu_87


# use sorted find the shortest sequence
def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))


# Because the number of incoming parameters is uncertain, you need to define variables dynamically
# use locals() or globals()
# use list comprehensions
def zip1(*args):
    for i in range(len(args)):
        globals()['iter' + str(i)] = args[i]

    return (tuple(globals()['iter' + str(i)][j] for i in range(len(args))) for j in shortest_sequence_range(*args))


if __name__ == '__main__':
    print(zip1([1, 2, 3], ["a", "b", "c"]))




