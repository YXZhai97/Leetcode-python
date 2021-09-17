# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:51:08 2021

@author: yixin
"""

#join the tuple with x
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

t=int(input())
s=list(input().split())
s.sort()
print(" ".join(s))