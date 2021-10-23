#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:45:43 2021

@author: yixing

https://www.nowcoder.com/test/question/c55f4f15cc3f4ff0adede7f9c69fa0c1?pid=31384776&tid=49350594

牛牛有一个数组，里面的数可能不相等，现在他想把数组变为：所有的数都相等。问是否可行。
牛牛可以进行的操作是：将数组中的任意一个数改为这个数的两倍。
这个操作的使用次数不限，也可以不使用，并且可以对同一个位置使用多次。

输入一个正整数N (N <= 50)
接下来一行输入N个正整数，每个数均小于等于1e9.

假如经过若干次操作可以使得N个数都相等，那么输出"YES", 否则输出"NO"

"""


n=int(input())
l=list(map(int,input().split()))
flag=0
dic=set()
for i in range(n):
    dic.add(l[i])
    for d in dic:
        if l[i]%d!=0 and d%l[i]!=0:
            flag=1
   
if flag==1:
    print("NO")
else:
    print("YES")