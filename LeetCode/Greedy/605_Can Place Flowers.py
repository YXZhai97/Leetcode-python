# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:29:06 2021

@author: yixing
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        plant=0
        flowerbed.extend([0,0])
        for i in range(len(flowerbed)-2):
            if flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]==0:
                flowerbed[i]=1
                plant+=1
        if plant>=n:
            return True 
        else:
            return False 