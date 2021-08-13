# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:36:23 2021

@author: yixin
"""

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                if i<j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix
                                

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(matrix)
s=Solution()
print(s.rotate(matrix))