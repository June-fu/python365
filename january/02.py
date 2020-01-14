# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/14

"""
最大公因数，也称最大公约数、最大公因子，指两个或多个整数共有约数中最大的一个。
02、如何求一个列表的最大公约数？
#示例:
#给定 nums = [2, 4, 6, 8]
#因为 2、4、6、8的最大公约数是2
#所以返回 2
"""
####
#利用辗转相除法，即欧几里得算法
#因为gcd(a,b,c)=gcd(gcd(a,b),c)=gcd(a,gcd(b,c))=gcd(gcd(a,c),b),所以定义gcd函数，然后成对数字利用辗转相除法；
####


def find_gcd(x, y):
    while y:
        x, y = y, x%y
    return x


nums = [2, 4, 6, 8]
gcd = find_gcd(nums[0], nums[1])
for i  in range(2, len(nums)):
    gcd = find_gcd(gcd, nums[i])
print(gcd)
