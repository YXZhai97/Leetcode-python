# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:47:18 2021

@author: yixing
"""

import sys

for line in sys.stdin:
    inlist=list(map(int,line.split()))
    print(sum(inlist))