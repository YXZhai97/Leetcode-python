# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:30:10 2021

@author: yixing
"""

t=int(input())
for i in range(t):
    num=list(map(int,input().split(" ")))
    print(sum(num[1:]))

