# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:51:48 2021

@author: yixing
"""

nums=[1,2,30,-4,-1,0,-1,-3,-4,5,22]



def sortlist(nums):
    l=len(nums)
    i=0
    j=l-1
    
    while i<j:
        if nums[j]>0:
            j-=1
            
        elif nums[j]<0 and nums[i]>0:
            nums[j],nums[i]=nums[i],nums[j]
            j-=1
            i+=1
        elif nums[j]<0 and nums[i]<0:
            j-=1
        
            
            
     
    
    return nums

print(sortlist(nums))