# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:18:14 2021

@author: yixing
"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp=[False]*(len(s)+1)     #[F,F,F,F,F,F,F]
        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
