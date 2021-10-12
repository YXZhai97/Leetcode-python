# -*- coding: utf-8 -*-
"""
Spyder Editor

edited by yixing 
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        record=[]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    record.append([i,j])
        for position in record:
            i=position[0]
            j=position[1]
            n=0
            m=0
            while n<c:
                matrix[i][n]=0
                n+=1
            while m<r:
                matrix[m][j]=0
                m+=1