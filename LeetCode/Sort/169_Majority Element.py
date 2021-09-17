# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 12:24:25 2021

@author: yixin
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sums={}
        maj=len(nums)//2
        for i in nums:
            if i not in sums:
                sums[i]=1
            else:
                sums[i]+=1
            if sums[i]>maj:
                return i
