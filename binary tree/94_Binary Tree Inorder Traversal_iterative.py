# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:04:04 2021

@author: yixing
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
       stack=[]
       result=[]
       while root is not None or stack!=[]:
           while root is not None:
               stack.append(root)
               root=root.left
           root=stack.pop()
           result.append(root.val)
           root=root.right 
       return result 
        
           
       