#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:51:47 2021

@author: yixing
"""


n=int(input())
ability=list(map(int,input().split()))
# pick k students, index distance less than d
k,d=map(int,input().split())

dp=[(any,any) for any in ability]

for i in range(1,k):
    dp1=dp[:i]
    for j in range(i,n):
        temp=[]
        for z in range(j-d,j):
            if z<0:
                continue
            else:
                temp.append(ability[j]*dp[z][0])
                temp.append(ability[j]*dp[z][0])
        dp1.append((max(temp),min(temp)))
    dp=dp1

print(max([max(each) for each in dp]))
