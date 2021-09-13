# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:53:37 2021

@author: yixin
"""

class Solution:
    def numIslands(self, grid):
        
        if not grid: return 0
        #空地地图返回0
        m=len(grid)
        n=len(grid[0])
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(i,j):
            grid[i][j]='0' #翻0
            
            for direc in direction:
                new_i,new_j = i+direc[0], j+direc[1]
                if new_i>=0 and new_i<m and new_j>=0 and new_j<n and grid[new_i][new_j]=='1':
                    dfs(new_i,new_j) #翻0
            return 
            
            
        
        counter= 0 #探索的次数
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    counter+=1
                    dfs(i, j)
        return counter