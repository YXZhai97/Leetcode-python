# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 19:06:34 2021

@author: yixin
"""
def removeDuplicates( nums):
        l=1 #left pointer 
        for r in range(1,len(nums)): #right pointer iterate through the list 
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l,nums[:l]

nums=[1,2,2,2,3,4,4,5,6,6]
print(removeDuplicates(nums))

