# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:43:02 2021

@author: yixing
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head 
        temp=[]
        
        while cur:
            temp.append(cur.val)
            cur=cur.next
        
        temp.sort()
        dummy=ListNode(0)
        cur=dummy 
        for v in temp:
            cur.next=ListNode(v)
            cur=cur.next
        
        return dummy.next