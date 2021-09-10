# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 22:12:19 2021

@author: yixing
"""
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    curA,curB=headA,headB
    a,b=0,0
    while curA:
        a+=1
        curA=curA.next
    while curB:
        b+=1
        curB=curB.next
    
    if a>b:
        curL=headA
        curS=headB
        diff=a-b
    else:
        curL=headB
        curS=headA
        diff=b-a
    
    i=0
    while i<diff:
        i+=1
        curL=curL.next
    while curL!=curS:
        curL=curL.next
        curS=curS.next
    
    return curL

        