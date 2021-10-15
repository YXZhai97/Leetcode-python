#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 19:59:57 2021

@author: yixing
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            
            for ch in s:
                count[ord(ch)-ord("a")]+=1
            
            
            res[tuple(count)].append(s)
        
        return res.values()