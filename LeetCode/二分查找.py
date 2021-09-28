# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:20:01 2021

@author: yixin
"""
'''
链接：https://www.nowcoder.com/questionTerminal/d732267e73ce4918b61d9e3d0ddd9182
来源：牛客网
'''
# 二分查找
'''
n天 m块巧克力，保证每天都有巧克力吃，第一天吃几块？ 
'''


n,m = map(int, input().split(" "))
  
def SumEat(e1,N):
    S = 0
    e = e1
    for i in range(0,N):
        S += e
        e = (e+1)//2
    return S
  
def BinarySearch(N,M):
    if N == 1:
        return M
    low = 1
    high = M
    while low<high:
        mid  = (low+high+1)//2
        if SumEat(mid,N)<=M:
            low = mid 
        else:
            high = mid -1
    return low
  
print(BinarySearch(n,m))