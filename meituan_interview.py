# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 10:40:34 2021

@author: yixin
"""
line=input()
num=int(input())
i=0
while i<num:
    numlist=list(map(int,input().split()))
    i+=1
    kk=0
    long=numlist[0]
    listsmall=line[:long]
    
    for k in range(1,long):
        if listsmall[0]==listsmall[k]:
            kk+=1
        if kk==numlist[1]:
            print(k)
            break
            
    if numlist[1]>kk:
        print(-1)