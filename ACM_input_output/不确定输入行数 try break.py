# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:07:07 2021

@author: yixin
"""

#预先不知道输入行数时

import sys
 
while True:
    try:
        string_hex = sys.stdin.readline()
        print(int(string_hex, 16))
    except:
        break

#或者


import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))