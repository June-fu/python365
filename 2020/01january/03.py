# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/15
"""
加入每年投入5000元，年化收益率是8%，按照复利计算，持续投资30年，本息共计多少钱？
Compound Interest = P(1 + R/100)~T
Where,
P is principle amount
R is the rate and
T is the time span
"""


# compound interest
def compound_interest(principle, rate, time):
    total_amount = 0
    while time:
        total_amount += principle * pow((1 + rate / 100), time)
        time -= 1
    return total_amount


if __name__ == '__main__':
    amount = compound_interest(5000, 10, 30)
    print("total amount is:", amount)
