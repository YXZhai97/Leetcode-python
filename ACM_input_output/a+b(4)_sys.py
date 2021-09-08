# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:56:34 2021

@author: yixin
"""

import sys
for line in sys.stdin:
    ls = line.split()
    if ls[0] != '0':
        print(sum(map(int,ls[1:])))