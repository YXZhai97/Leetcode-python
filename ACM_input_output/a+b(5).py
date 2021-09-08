# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:34:05 2021

@author: yixing
"""

t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    summ=sum(a[1:])
    print(summ)