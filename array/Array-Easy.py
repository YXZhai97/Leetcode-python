# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:35:06 2021

@author: yixing
"""
class Solution:
    def longestCommonPrefix(self, strs) :
        strlen_min=min([len(s) for s in strs])
        prefix = ""
    
        for i in range(strlen_min):
            
            char=list(set([s[i] for s in strs]))
        
            if len(char)==1:
                prefix+=char[0]
            else:
                break 
        return prefix 
    

strs = ["flower","flow","flight"]

ss=Solution()
print(ss.longestCommonPrefix(strs))


        