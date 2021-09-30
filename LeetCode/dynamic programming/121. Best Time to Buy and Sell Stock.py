# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:44:15 2021

@author: yixing
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left=0
        right=1
        incomemax=0
        for right in range(1,len(prices)):
            if prices[right]>prices[left]:
                incomemax=max(incomemax,prices[right]-prices[left])
            else:
                left=right
                right+=1
        return incomemax
