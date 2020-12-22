# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/27
"""
python-practice-book 11
Write a function dups to find all duplicates in the list.
input: dups([1, 2, 1, 3, 2, 5])
output: [1, 2]
"""


# 11-Write a function dups to find all duplicates in the list.
def dups(list1):
    list_two = []
    for i in list1:
        if list1.count(i) > 1 and i not in list_two:
            list_two.append(i)

    return list_two


def dups2(list1):
    import collections
    return [item for item, count in collections.Counter(list1).items() if count > 1]


def dups3(list1):
    seen = set()
    return [x for x in list1 if list1.count(x) > 1 and x not in seen and not seen.add(x)]


def dups4(list1):
    dict_1 = {}
    list2 = []
    for i in list1:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            if dict_1[i] == 1:
                list2.append(i)
            dict_1[i] += 1
    return list2


# no matter what in the list;
# If list elements are not hashable;you cannot use sets/dicts and have to resort to a quadratic time solution
def dups5(list1):
    return [x for n, x in enumerate(list1) if x in list1[:n]]


if __name__ == '__main__':
    print(dups([1, 2, 1, 3, 2, 5]))
    print(dups2([1, 2, 1, 3, 2, 5]))
    print(dups3([1, 2, 1, 3, 2, 5]))
    print(dups4([1, 2, 1, 3, 2, 5]))

    a = [[1], [2], (3, 4), [1], [5], (3, 4)]
    print(dups5(a))
