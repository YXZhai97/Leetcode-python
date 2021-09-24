# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:00:59 2021

@author: yixing
"""

'''
链接：https://www.nowcoder.com/questionTerminal/11ee0516a988421abf40b315a2b28d08
来源：牛客网
'''

fa = list(range(1000001))   
size = [1] * 1000001       
def init():
    for i in range(1000001):
        fa[i] = i
        size[i] = 1
 
 
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])  # 递归查找根节点
    return fa[x]
 
 
def merge(x,y):
    fx = find(x)
    fy = find(y)
    if fx!=fy:
        fa[fy] = fx
        size[fx] += size[fy]
 
 
def main():
    T = int(input("测试数据组T:"))
    for i in range(T):
        n = int(input("圈子数n："))
        init()
        res = 1
        for j in range(n):
            a,b = list(map(int, input("输入圈子里的编号：").split()))
            merge(a,b)
            res = max(res,size[find(a)])
 
        print(res)
 
main()