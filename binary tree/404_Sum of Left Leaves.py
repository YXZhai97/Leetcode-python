# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:49:40 2021

@author: yixing
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        self.sum=0
        
        def dfs(root):
            if root is None:
                return 0
            if root.left:
                if isLeave(root.left):
                    self.sum+=root.left.val 
            dfs(root.left)
            dfs(root.right)
            
        
        def isLeave(root):
            if not root.left and not root.right:
                return True
            else:
                return False 
        dfs(root)
        return self.sum