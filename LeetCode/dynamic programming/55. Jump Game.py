# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:26:03 2021

@author: yixing
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last=len(nums)-1
        maxj=0
        for i in range(len(nums)):
            if i>maxj:
                return False 
            if i+nums[i]>maxj:
                maxj=i+nums[i]
            if maxj>=last:
                return True 