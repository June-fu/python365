# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/19
"""
Python Program for array rotation
Write a function rotate(ar[], d) that rotates arr[] by d elements.

Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2
Output arr[] = [3, 4, 5, 6, 7, 1, 2]
"""


def left_rotate(arr, d):
    i = 0
    while i < d:
        arr.append(arr[0])
        del arr[0]
        i += 1
    return arr


# 递归实现
def left_rotate2(arr, d):
    for i in range(d):
        left_rotate_one(arr)
    return arr


def left_rotate_one(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    print(left_rotate(arr1, 2))
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    print(left_rotate2(arr2, 2))

