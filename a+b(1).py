# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:46:33 2021

@author: yixin
"""
while True:
    try:
        num=list(map(int,input().split(' ')))
        print(num[0]+num[1])
    except:
        break 