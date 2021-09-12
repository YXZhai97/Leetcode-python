# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:21:01 2021

@author: yixing
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        #helper() 从中间开始向两边 搜索
        def helper(l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        
        res=""
        
        for i in range(len(s)):
            test=helper(i,i)
            if len(test)>len(res):
                res=test
                
            test=helper(i,i+1)
            if len(test)>len(res):
                res=test
                
        return res 