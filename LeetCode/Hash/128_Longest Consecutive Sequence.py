#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:01:25 2021

@author: yixing
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        l=len(nums)
        i=0
        counter=1
        maxcounter=1
        while i<l-1:
            if nums[i+1]-nums[i]==1:
                i+=1
                counter+=1
                if counter >= maxcounter:
                    maxcounter=counter 
            elif nums[i+1]==nums[i]:
                i+=1
                
            else: 
                counter=1
                i+=1
        return maxcounter