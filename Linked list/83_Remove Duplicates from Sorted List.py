# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:44:54 2021

@author: yixing
"""

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur=head 
    while cur and cur.next:
        if cur.val==cur.next.val:
            cur.next=cur.next.next
        else:
            cur=cur.next
        
    return head 