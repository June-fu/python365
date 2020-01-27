# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/27
"""
python-practice-book 8
Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
Write a function cumulative_sum to compute cumulative sum of a list.
Does your implementation work for a list of strings?
"""


# from 10.py
def sum(list_one):
    if type(list_one[0]) is int:
        total = 0
        for i in list_one:
            total += i
        return total
        assert type(list_one[0]) is str, print("OMG, the elements of this list is str !")
    elif type(list_one[0]) is str:
        total = ''.join(list_one)
        return total
    else:
        return None


def cumulative_sum(list_one):
    list_two = []
    for i in range(0, len(list_one)):
        list_two.append(sum(list_one[0:i+1]))
        # list_two[i] = sum(list_one[0:i+1])  # this is wrong!!!!
    return list_two


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print(cumulative_sum(list1))

    list2 = [4, 3, 2, 1]
    print(cumulative_sum(list2))
