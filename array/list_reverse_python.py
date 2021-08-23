# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:46:39 2021

@author: yixin
"""

#The reverse() method doesn't return any value. It updates the existing list.
m=[1,2,3,4,5]
print(m)
m.reverse()
print(m)
matrix=[[1,2,3,4,5],
        [2,3,4,5,6],
        [3,4,5,6,7]]
for row in matrix:
    row.reverse()
print(matrix)