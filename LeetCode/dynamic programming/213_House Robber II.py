#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 22:20:58 2021

@author: yixing
"""

from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(sub_nums):
            dp=[each for each in sub_nums]
            n=len(sub_nums)
            for i in range(2,n):
                dp[i]+=max(dp[:i-1])
        
            return max(dp)
        
        if len(nums)<4:
            return max(nums)
        else:
            return max(helper(nums[1:]),helper(nums[:-1]))