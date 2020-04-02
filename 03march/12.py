#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/31
"""
itertools — Functions creating iterators for efficient looping
The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.

Iterators terminating on the shortest input sequence:
accumulate(p[, func]) --> p0, p0+p1, p0+p1+p2
chain(p, q, ...) --> p0, p1, ... plast, q0, q1, ...
chain.from_iterable([p, q, ...]) --> p0, p1, ... plast, q0, q1, ...
compress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ...
dropwhile(pred, seq) --> seq[n], seq[n+1], starting when pred fails
groupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v)
filterfalse(pred, seq) --> elements of seq where pred(elem) is False
islice(seq, [start,] stop [, step]) --> elements from
       seq[start:stop:step]
starmap(fun, seq) --> fun(*seq[0]), fun(*seq[1]), ...
tee(it, n=2) --> (it1, it2 , ... itn) splits one iterator into n
takewhile(pred, seq) --> seq[0], seq[1], until pred fails
zip_longest(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ...
"""
import operator


def accumulate(iterable, func=operator.add, *, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total


# 152773.82975208995
# 20万贷款，分期3年，按月还款，年利率4.65%，每月还款2000，最后一次还款多少？
def last_payment(total, month_pay, rate, year):
    from itertools import repeat
    month_payment = [e for e in repeat(- month_pay, year * 12)]
    print([a for a in accumulate([total] + month_payment, lambda x, y: x * (1 + rate / 100 / 12) + y)][year * 12])


if __name__ == '__main__':
    print([x for x in accumulate([1, 2, 3, 4, 5], operator.mul)])

    data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    # running max
    print(list(accumulate(data, max)))

    # Amortize a 5% loan of 1000 with 4 annual payments of 90
    cashflows = [1000, -90, -90, -90, -90]
    print([s for s in accumulate(cashflows, lambda a, b: a * 1.05 + b)])

    last_payment(200000, 2000, 4.65, 3)

    logistic_map = lambda x, _:  r * x * (1 - x)
    r = 3.8
    x0 = 0.4
    from itertools import repeat
    inputs = repeat(x0, 36)  # only the initial value is used
    print([format(x, '.2f') for x in accumulate(inputs, logistic_map)])
