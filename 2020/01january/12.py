# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/27
"""
python-practice-book 10
Write a function unique to find all the unique elements of a list
input: unique([1, 2, 1, 3, 2, 5])
output: [1, 2, 3, 5]
"""


# 10-Write a function unique to find all the unique elements of a list
def unique(list_one):
    list_two = []
    for i in list_one:
        if i not in list_two:
            list_two.append(i)
    return list_two


def unique2(list_one):
    import collections
    return [i for i in collections.Counter(list_one).keys()]
    # return [i for i, count in collections.Counter(list_one).items() if count == 1]


def unique3(list_one):
    seen = set()
    return [x for x in list_one if x not in seen and not seen.add(x)]


def unique4(list_one):
    return list(set(list_one))


def test():
    s = set()
    for i in range(3):
        if not s.add(i):
            print(s)


if __name__ == '__main__':
    print(unique([1, 2, 1, 3, 2, 5]))
    print(unique2([1, 2, 1, 3, 2, 5]))
    print(unique3([1, 2, 1, 3, 2, 5]))
    print(unique4([1, 2, 1, 3, 2, 5]))
    test()


