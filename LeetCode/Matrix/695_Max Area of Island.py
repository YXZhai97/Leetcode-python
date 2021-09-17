# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:25:52 2021

@author: yixing
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        maxArea=0
        row,col=len(grid),len(grid[0])
        visited=[[False for i in range(col)] for j in range(row)]
        direction=[[0,-1],[0,1],[-1,0],[1,0]]
    
        
        def dfs(i,j):
            
            if visited[i][j]:
                return 0
            visited[i][j]=True 
            currentArea=1
            for direc in direction:
                newI, newJ =i+ direc[0], j+direc[1]
                if newI>=0 and newI<=row-1 and newJ>=0 and newJ<=col-1 and grid[newI][newJ]==1:
                    currentArea+=dfs(newI,newJ)
            
            return currentArea
            
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    maxArea=max(maxArea, area)
        return maxArea
        
        