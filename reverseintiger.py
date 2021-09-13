# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:59:42 2021

@author: yixing
"""

def revo(num):
    rev=0
    while num>0:
        pop=num%10
        rev=rev*10+pop 
        num=num//10
    return rev


num=12378
print(revo(num))


num=100
print(str(num)[1])