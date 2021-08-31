# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:55:55 2021

@author: yixing
"""

while True:
    num=list(map(int,input().split()))
    if num[0]==0:
        break
    else:
        print(sum(num[1:]))
        