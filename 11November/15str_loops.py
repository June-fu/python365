#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-07 22:20:41
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-07 22:21:24
 # @ Description:
 https://www.hackerrank.com/challenges/30-review-loop/problem
 '''

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        rt1 = rt2 =''
        st = input()
        for j in range(len(st)):
            if ~j % 2:
                rt1 += st[j]
            else:
                rt2 += st[j]
        print('{0} {1}'.format(rt1, rt2))
            