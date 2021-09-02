# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:38:23 2021

@author: yixing
"""

import sys

for line in sys.stdin:
    temp=list(map(int,line.split()))
    print(sum(temp[1:]))
    