# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:04:06 2021

@author: yixing

背包问题
"""
'''
k=int(input())
a,x,b,y=list(map(int,input().split()))

链接：https://www.nowcoder.com/questionTerminal/f3ab6fe72af34b71a2fd1d83304cbbb3
来源：牛客网

链接：https://www.nowcoder.com/questionTerminal/f3ab6fe72af34b71a2fd1d83304cbbb3
来源：牛客网

小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，
现在小Q想用这些歌组成一个总长度正好为K的歌单，
每首歌最多只能在歌单中出现一次，在不考虑歌单内歌曲的先后顺序的情况下，请问有多少种组成歌单的方法。

链接：https://www.nowcoder.com/questionTerminal/f3ab6fe72af34b71a2fd1d83304cbbb3
来源：牛客网

每个输入包含一个测试用例。
每个测试用例的第一行包含一个整数，表示歌单的总长度K(1<=K<=1000)。
接下来的一行包含四个正整数，分别表示歌的第一种长度A(A<=10)和数量X(X<=100)
以及歌的第二种长度B(B<=10)和数量Y(Y<=100)。保证A不等于B。
'''

k = int(input().strip())
lx, x, ly, y = list(map(int, input().strip().split(" ")))
  
dp = [1] + [0] * k  # 第一位初始化为1
for i in range(x):
    for j in range(k, lx-1, -1):
        dp[j] += dp[j-lx]
          
for i in range(y):
    for j in range(k, ly-1, -ly):  # 第二次步长为ly
        dp[j] += dp[j-ly]
print(dp[k]%1000000007)



