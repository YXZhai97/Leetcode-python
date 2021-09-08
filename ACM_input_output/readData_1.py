# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:16:59 2021

@author: yixin
"""

import sys 

while True:
    try:
        number=sys.stdin.readline().strip()
        number=number.split("")
        a=int(number[0])
        b=int(number[1])
        print(a+b)
    except:
        break
    
