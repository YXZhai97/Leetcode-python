# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:55:42 2021

@author: yixing
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        t=sorted(t)
        s=sorted(s)
        if len(t)!=len(s):
            return False 
    
        for i in range(len(t)):
            if t[i]!=s[i]:
                return False 
        return True