# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 20:21:24 2021

@author: yixin
"""
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        '''
         2         11
        3 4       9 10
       6 5 7     7 6 10
      4 1 8 3   4 1 8 3
        '''
        
        layer=len(triangle)
        
        for i in range(layer-2,-1,-1):
            for j in range(i+1):
                left=triangle[i+1][j]+triangle[i][j]
                right=triangle[i+1][j+1]+triangle[i][j]
                triangle[i][j]=min(left,right)
                
        return triangle[0][0]
        
    