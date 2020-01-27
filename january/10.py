# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/27
"""
solve the problem in python-practice-book
https://anandology.com/python-practice-book/working-with-data.html
problem 2-5
"""


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


# Implement a function product, to compute product of a list of numbers.
def product(list_two):
    total_product = 1
    for i in list_two:
        total_product *= i
    return total_product


# Write a function factorial to compute factorial of a number( use the product function defined before)
def factorial(integer):
    return product(range(1, integer + 1))


if __name__ == '__main__':
    list1 = [1, 2, 3]
    total_sum = sum(list1)
    print(total_sum)
    print(sum(['a', 'b', 'c']))
    print(product(list1))
    print(factorial(4))
