# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/26
"""
how to iterate over two lists together--using the built-in function zip

zip function:
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences
or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument,
it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.



"""


def list_together(n, v):
    for name, value in zip(n, v):
        print(name, value)


# Passing Arguments of Unequal Length
def list_tg_unequal():
    integers = [1, 2, 3]
    letters = ['b', 'c', 'a']
    floats = [4.0, 5.0, 6.0, 7.0]
    print(list(zip(integers, letters, floats)))
    return zip(integers, letters, floats)


def list_tg_longest():
    from itertools import zip_longest

    integers = [1, 2, 3]
    letters = ['a', 'b', 'c']
    floats = [4.0, 5.0, 6.0, 7.0]
    print(list(zip_longest(integers, letters, floats, fillvalue="?")))


if __name__ == '__main__':
    names = ["a", "b", "c"]
    values = [1, 2, 3]
    list_together(names, values)
    list_tg_unequal()
    list_tg_longest()

    # Traversing Dictionaries in Parallel
    dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
    dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
    for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
        print(k1, '->', v1)
        print(k2, '->', v2)

    # unzip a sequence
    a = list_tg_unequal()
    print("a", a)
    # in python3 zip() returns an iterator. This object yields tuples on demand and can be traversed only once.
    # so if list(a) is executed then the remaining code will produce an error
    # print("list_A:", list(a))
    i, l, f = zip(*a)
    print('i:', i)
    print('l:', l)
    print('f:', f)

    # sorting in parallel
    letters = ['b', 'a', 'd', 'c']
    numbers = [2, 4, 3, 1]
    print(zip(letters, numbers))
    print(sorted(zip(letters, numbers)))
    print(sorted(zip(numbers, letters)))

    # Building Dictionaries
    fields = ['name', 'last_name', 'age', 'job']
    values = ['John', 'Doe', '45', 'Python Developer']
    dict_3 = dict(zip(fields, values))
    print(dict_3)

    # update an existing dictionary by combining zip()
    new_age = [18]
    field = ['age']
    dict_3.update(zip(field, new_age))
    print(dict_3)







