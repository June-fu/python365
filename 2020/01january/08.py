# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/26
"""
using assertions in Python
assert_stmt ::= "assert" expression1 ["," expression2]
the proper use of assertions is to inform developers about unrecoverable errors in a program.
Common Pitfalls:
    Don’t Use Asserts for Data Validation--assertions can be globally disabled
    Asserts That Never Fail--if a tuple is the first argument then the assertion always evaluates as true and therefore never fails.
Key Takeaways:
    • Python’s assert statement is a debugging aid that tests a condition as an internal self-check in your program.
    • Asserts should only be used to help developers identify bugs. They’re not a mechanism for handling run-time errors.
    • Asserts can be globally disabled with an interpreter setting.
"""


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


if __name__ == '__main__':
    shoes = {'name': 'Fancy Shoes', 'price': 14900}
    shoes_price = apply_discount(shoes, 0.7)
    print(shoes_price)
