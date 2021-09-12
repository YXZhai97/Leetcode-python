# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:22:19 2021

@author: yixin
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        if len(nums)<=2:
            return res
        
        if len(nums)==3:
            return nums[0] + nums[1] + nums[2]
        
        nums.sort()
        # print(nums)
        
        c = float("inf")   #定义一个大数作为初始化
        sum_ = 0
        for i in range(len(nums)):
            
            # if i>0  and nums[i] == nums[i-1]:
            #     continue
            
            low = i+1
            high = len(nums) - 1
            
            while low<high:
                # print(nums[i], nums[low], nums[high])
                temp_sum = nums[i]+nums[low]+nums[high]
                if temp_sum > target:
                    if temp_sum-target<c:
                        c = int(temp_sum-target)
                        sum_ = temp_sum
                    high-=1
                elif temp_sum < target:
                    if target-temp_sum<c:
                        c = int(target-temp_sum)
                        sum_ = temp_sum
                    low+=1
                else:
                    sum_ = temp_sum
                    return sum_
        return sum_
        