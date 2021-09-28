# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:45:35 2021

@author: yixin
"""
'''
牛牛和羊羊正在玩一个纸牌游戏。这个游戏一共有n张纸牌, 第i张纸牌上写着数字ai。
牛牛和羊羊轮流抽牌, 牛牛先抽, 每次抽牌他们可以从纸牌堆中任意选择一张抽出, 直到纸牌被抽完。
他们的得分等于他们抽到的纸牌数字总和。
现在假设牛牛和羊羊都采用最优策略, 请你计算出游戏结束后牛牛得分减去羊羊得分等于多少。
'''


n=int(input())
nums=list(map(int,input().split()))
nums=sorted(nums)
nums.reverse()
nn=0
yy=0
for i in range(len(nums)):
    if i%2==0:
        nn+=nums[i]
    else:
        yy+=nums[i]
print(nn-yy)
