# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:11:44 2021

@author: yixing
"""

class Solution:
    def maxProfit(self, prices) -> int:
        gain=0
        length=len(prices)-1
        for i in range(length):
            if prices[i]<prices[i+1]:
                gain+=prices[i+1]-prices[i]
        return gain
                
            