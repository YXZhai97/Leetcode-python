# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:04:18 2021

@author: yixing
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
       
        row=len(grid)
        col=len(grid[0])
        dp=[[0]*col for i in range(row)]
        dp[0][0]=grid[0][0]
        
        #initialize first row 
        for i in range(1,row):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        #initialize first col
        for j in range(1,col):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        
        for i in range(1,row):
            for j in range(1,col):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        
        return dp[row-1][col-1]
                
    
            
    
        