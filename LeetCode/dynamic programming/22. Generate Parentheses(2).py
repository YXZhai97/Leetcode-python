# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:48:31 2021

@author: yixing
"""

def generateParenthesis(n) :
        
    stack=[]
    res=[]
        
    def backtrack(openN,closedN):
        if openN==closedN==n:
            res.append("".join(stack))
            return 
            
        if openN<n:
            stack.append("(")
            backtrack(openN+1,closedN)
            stack.pop()
            
        if closedN<openN:
            stack.append(")")
            backtrack(openN,closedN+1)
            stack.pop()
                
    backtrack(0,0)
            
    return res

generateParenthesis(3)
