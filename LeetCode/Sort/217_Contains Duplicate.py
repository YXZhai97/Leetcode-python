# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:03:16 2021

@author: yixing
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dic={}
        for a in nums:
            if a not in dic:
                dic[a]=1
            else:
                return True 
        
        return False 