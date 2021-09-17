# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:09:44 2021

@author: yixing
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        dic={
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000,
            
        }
        output=[]
        for i,j in reversed(dic.items()):
            while num>0:
                if j<=num:
                    output.append(i)
                    num-=j
                else:
                    break
        return "".join(output)

