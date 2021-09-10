# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:44:52 2021

@author: yixing
"""

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited=set()
        cura,curb=headA,headB
        while cura:
            visited.add(cura)
            cura=cura.next
        
        while curb:
            if curb in visited:
                return curb
            curb=curb.next
    
        return None 
                