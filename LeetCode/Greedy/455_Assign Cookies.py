# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:46:30 2021

@author: yixing
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child=0
        g=sorted(g)
        s=sorted(s)
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j]>=g[i]:
                    child+=1
                    s.pop(j)
                    break 
        return child 