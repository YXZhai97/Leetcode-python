# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:32:49 2021

@author: yixing
"""



while True:
    try:
        m = int(input())
        tmp = list(map(int,input().split(' ')))
        tmp2 = set(tmp)
        tmp3 = list(tmp2)
        tmp3.sort()
        if len(tmp3) >= 3:
            print(tmp3[2])
        else:
            print(-1)
    except:
        break
