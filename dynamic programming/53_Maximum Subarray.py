# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:07:18 2021

@author: yixing
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        cur_sum=0
        
        for n in nums:
            cur_sum=max(cur_sum+n,n)
            max_sum=max(max_sum,cur_sum)
            
        return max_sum