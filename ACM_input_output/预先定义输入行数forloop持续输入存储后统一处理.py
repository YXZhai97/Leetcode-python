# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:24:10 2021

@author: yixin
"""

#预先定义输入行数 n 

while True:
    try:
        n=int(input())  #预先定义输入行数
        r=[]
        for i in range(n):       
            r.append(int(input()))  #在for-loop里实现持续输入 存储在r 
        for i in sorted(set(r)):  #程序本体
            print(i)
    except:
        break  #跳出输入循环