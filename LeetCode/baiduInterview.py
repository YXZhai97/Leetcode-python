# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:57:03 2021

@author: yixing
"""

124
134

list=[-2,1, -3, 4 ,-1 ,2 ,1 ,-5, 4 ]

def iscontinue(self,numlist):
    length=len(numlist)
    sumlist=[]
    sum=0
    for j in range(length):
        
        for i in range(j,length):
            sum=numlist[i]
            if numlist[i+1]-numlist[i]==1:
                sum+=numlist[i+1]
            else:
                sumlist.append(sum)
                sum=0
                break 
            
    return max(sumlist)

