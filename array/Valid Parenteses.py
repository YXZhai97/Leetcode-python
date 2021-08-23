# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:09:55 2021

@author: yixing
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(","]":"[","}":"{" }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return True if not stack else False 
            
            
s=Solution()
strs= "()[]{()}}"
print(s.isValid(strs))
         
        