# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:01:37 2021

@author: yixing
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_list=list(t)
        for char in s:
            t_list.remove(char)
        return t_list[0]
    
