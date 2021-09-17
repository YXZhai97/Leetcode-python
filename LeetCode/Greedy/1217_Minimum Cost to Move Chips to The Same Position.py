# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:16:11 2021

@author: yixin
"""
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        position1=0
        position2=0
        for chip in position:
            if chip%2==0:
                position2+=1
            else:
                position1+=1
        if position1>position2:
            return position2
        else: 
            return position1 