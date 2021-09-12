# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 23:33:35 2021

@author: yixing
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack=list(s)
        
        for char in t:
            if stack and stack[0]==char:
                stack.pop(0)
                
        return stack==[]