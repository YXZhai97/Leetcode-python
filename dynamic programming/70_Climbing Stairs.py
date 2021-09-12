# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:51:55 2021

@author: yixing
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        #0 1 2 3 4 5 6 7 8
        #  1 2 3 5
        
        if n<=2:
            return n
        pre1=1
        pre2=2
        
        for i in range(2,n):
            current=pre1+pre2
            pre1=pre2
            pre2=current
        
        return current 
    
    
    
    
