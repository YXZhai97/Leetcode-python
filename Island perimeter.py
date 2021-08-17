# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:19:36 2021

@author: yixing
"""

class Solution:
    def islandPerimeter(self, grid):
        nrow,ncol=len(grid),len(grid[0])
        perimeter=0
        for r in range(nrow):
            for c in range (ncol):
                if grid[r][c]:
                    perimeter+=4
                    if r>0 and grid[r-1][c]==1:
                        perimeter-=1
                    if r<nrow-1 and grid[r+1][c]==1:
                        perimeter-=1
                    if c>0 and grid[r][c-1]==1:
                        perimeter-=1
                    if c<ncol-1 and grid[r][c+1]==1:
                        perimeter-=1
            
        return perimeter 

s=Solution()
grid=[[0,1,0,0]]
print(s.islandPerimeter(grid))