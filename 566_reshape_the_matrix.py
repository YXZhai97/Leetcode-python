# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:58:07 2021

@author: yixin
"""

class Solution:
    def matrixReshape(self, mat, r, c) :
        row=len(mat)
        col=len(mat[0])
        new=[]
        if col*row!=r*c:
            return mat
        total= [mat[i][j] for i in range(row) for j in range(col)]
        new=[[total[c*j+i] for i in range(c)] for j in range(r)]
        return new 