# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:59:28 2021

@author: yixin
"""

a=[1,0,1,0,0,1,1,1,0,1,0,1]
length=len(a)
n=length-1
while n>1:
        for i in range(length-n):
            for j in range(i+1,length-n):
                if sum(a[i:i+n])==sum(a[j:j+n]):
                    print(i+1,i+n+1,j+1,j+n+1)
                    break
            else:
                break
            
            
        n-=1