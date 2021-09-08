# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:49:46 2021

@author: yixing
"""

while True:
    num=input().split()
    num1=int(num[0])
    num2=int(num[1])
    if num1==num2==0:
        break
    else:
        print(num1+num2)
