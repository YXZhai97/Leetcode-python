# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:44:39 2021

@author: yixin
"""



import math
 
def is_color(a,b,c):
    if a==b==c or(a!=b and a!=c and b!=c):
        return True
    else:
        return False
 
def cross_product(a,b,c):
    """
    S = |AB x AC|/2
    """
    ab = [b[i]-a[i] for i in range(3)]
    ac = [c[i]-a[i] for i in range(3)]
    i = ab[1]*ac[2]-ab[2]*ac[1]
    j = ab[2]*ac[0]-ab[0]*ac[2]
    k = ab[0]*ac[1]-ab[1]*ac[0]
    S = math.sqrt(i**2+j**2+k**2) / 2
    return S
 
N = int(input().strip())
points = []
colors = []
res = 0
for _ in range(N):
    line = input().strip().split()
    colors.append(line[0])
    points.append([int(x) for x in line[1:]])
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if is_color(colors[i], colors[j], colors[k]):
                res = max(res, cross_product(points[i], points[j], points[k]))
 
# print(f'{res:.5f}')
print('%.5f' % res)