# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:34:32 2021

@author: yixing
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen=set()
        cur=head 
        while cur:
            if cur in seen:
                return True 
            seen.add(cur)
            cur=cur.next
        return False