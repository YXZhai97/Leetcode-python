# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 19:59:21 2021

@author: yixing
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums)-1]<target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]>=target:
                return i