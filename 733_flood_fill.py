# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:23:19 2021

@author: yixing
"""
class Solution:
    def floodFill(self, image, sr, sc, newColor) :
        R,C=len(image),len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r,c):
            if image[r][c]==color:
                image[r][c]=newColor
                if r>=1: dfs(r-1,c)
                if r+1<R: dfs(r+1,c)
                if c>=1: dfs(r,c-1)
                if c+1<C: dfs(r,c+1)
        dfs(sr,sc)
        return image 


image=[[1,1,1],[1,1,0],[1,0,1]]
print(image)
sr=1
sc=1
newColor=2
s=Solution()
print(s.floodFill(image, sr, sc, newColor))