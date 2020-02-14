#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/13
"""
海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
"""


# 思考num为最后一只猴子拿到的桃子数量，那么轮到最后一只猴子的时候桃子个数为：(num * 5 + 1)
# 第四只拿到的就是：(num * 5 + 1)//4;因此反推到第一个猴子拿的时候桃子的个数即为原来桃子个数
# 那么除了第一个猴子，每个猴子面前的桃子都能被4整除
def divide_peach():
    for num in range(1000):
        for x in range(5):
            num = num * 5 + 1
            if not num % 4:
                num = num // 4
                continue
            else:
                break

        if x == 4:
            return num
    return None


# 用递归求出第m个猴子拿走的桃子个数
# 假设总数为num，第一个猴子就拿掉(num - 1) // 5 个，后续每个猴子都是在总数减去上一个猴子拿走的再减去扔到海里的一个
def get_peach(num, m):
    if (num - 1) % 5:  # num - 1 肯定可以被5整除
        return 0
    result = (num - 1) // 5  # 保证返回值是int
    if m == 1:
        return result
    else:
        return get_peach(num - result - 1, m - 1)


def divide_peach2():
    for num in range(1, 1000):
        num = num * 5 + 1  # 别小看这一句，省掉了上千次的循环
        total = 0
        for i in range(1, 6):
            total = total + get_peach(num, i) + 1  # 每次都加上扔到海里的一个
            if not get_peach(num, i):  # 返回值为0 ，说明num - 1 不可以被5整除
                break
            if i == 5:
                total += get_peach(num, i) * 4  # 加上最后剩余的4份
        if total == num:
            return total


# 假设最后一个猴子拿完后还剩下x个桃子，那么轮到最后一只猴子的时候桃子个数为：(x / 4 * 5 + 1)
# 逆向倒推到轮到第一只猴子的时候即为原来的桃子个数
# 很明显剩下的桃子（x）是可以被4整除的
def divide_peach3():
    i = 0
    j = 1  # 最终剩余的必然是4的倍数，从剩余的开始，循环次数最少
    while i < 4:  # 若 i==4 说明下面的for循环已经运行完成整个循环
        x = 4 * j
        for i in range(5):
            if x % 4:   # 若不能整除，说明错误，跳出循环
                i = i - 1  # 很重要！！！防止最后一次循环的时候跳出；其实循环没有完成但是i也等于4
                break
            x = x / 4 * 5 + 1
        j += 1
    return x


if __name__ == '__main__':
    print(divide_peach())
    print(divide_peach2())
    print(divide_peach3())

