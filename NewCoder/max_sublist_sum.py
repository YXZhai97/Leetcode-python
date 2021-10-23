#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:41:46 2021

@author: yixing

max sub list sum 
"""

nums=[1,-2,3,4,-7,0,3,5,6]

dp=nums
for i in range(1,len(dp)):
    if dp[i-1]>0:
        dp[i]+=dp[i-1]
print(max(dp))
print(dp)
