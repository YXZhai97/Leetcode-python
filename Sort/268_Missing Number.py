# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:56:22 2021

@author: yixing
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)+1):
            if i not in nums:
                return i 
            
            
    
    
class Solution2:
    def missingNumber2(self, nums: List[int]) -> int:
        
        summ=sum(nums)
        add=0
        for i in range(len(nums)+1):
            add=add+i
        return add-summ
            