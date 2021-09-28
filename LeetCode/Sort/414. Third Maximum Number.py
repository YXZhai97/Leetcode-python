# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:11:30 2021

@author: yixin
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        
        if len(nums)<3:
            return max(nums)
    
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
