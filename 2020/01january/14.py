# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/27
"""
python-practice-book 12
Write a function group(list, size) that take a list and splits into smaller lists of given size.
input:  group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
output: [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
"""


def group(list1, size):
    # return [list1[i::size] for i in range(size)]
    list_one = []
    if int(len(list1) % size) == 0:
        x = int(len(list1)/size)
    else:
        x = int(len(list1)/size) + 1
    for i in range(x):
        list_one.append(list1[i * size:(i+1) * size])
    return list_one


# use slice
def group1(list1, size):
    return [list1[i:i+size] for i in range(0, len(list1), size)]


if __name__ == '__main__':
    print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
    print(group1([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))



