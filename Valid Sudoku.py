# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:20:05 2021

@author: yixing
"""

class Solution:
    def isValidSudoku(self, board) :
        valid=self.row_valid(board) and self.col_valid and self.squr_valid(board)
        return vakid 
    
    def row_valid(self,board):
        for row in board:
            if not self.is_unit_valid(row):
                return False 
        return True 
    
    
    def col_valid(self,board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False 
        
        
        return True
        
    
    
    def squr_valid(self,board):
        for i in (0,3,6):
            for j in (0,3,6):
                square=[board[x][y] for x in range (i,i+3) for y in range(j,j+3) ]
                if not self.is_unit_valid(square):
                    return False 
        
        return True 
    
    def is_unit_valid(self,unit):
        unit=[i for i in unit if i!='.']
        return len(set(unit))==len(unit) and len(set(unit))!=0

board=[["5","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]

square=[board[x][y] for x in range (0,3) for y in range(0,3) ]
print(square)
print(board)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(tuple(x))

