#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 10:47:44 2021

@author: yixing
链接：https://www.nowcoder.com/questionTerminal/11ee0516a988421abf40b315a2b28d08
来源：牛客网
"""

class UnionFind(object):
     
    def __init__(self):    
        self.parent=[i for i in range(10**7+1)]
        self.parentnums=[1]*(10**7+1)
 
    def find(self,x):
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]  #路径压缩
            x=self.parent[x]
        return x
 
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx==rooty:
            return
        self.parent[rooty]=rootx
        self.parentnums[rootx]+=self.parentnums[rooty]
 
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        n=int(input())
        uf=UnionFind()
        params=[]
        for _ in range(n):
            params=list(map(int,input().split()))
            x,y=int(params[0]),int(params[1])
            uf.union(x,y)
        maximum=0
        for i in range(1,len(uf.parentnums)):
            maximum=max(maximum,uf.parentnums[i])
        print(maximum)