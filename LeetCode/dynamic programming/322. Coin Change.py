# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:18:46 2021

@author: yixin
"""
from typing import List 

def coinChange(coins: List[int], amount: int) -> int:
        combi=[1]+[0]*amount
        for coin in coins:
            for am in range(amount+1):
                if am>=coin:
                    combi[am]+=combi[am-coin]
        return combi[-1]
coins=[1,2,5]
amount=11
coinChange(coins, amount)


def coinChange(self, coins: List[int], amount: int) -> int:
       combi=[0]+[float('inf')]*amount
       for coin in coins:
            for am in range(amount+1):
                if am>=coin:
                    combi[am]=min(combi[am],combi[am-coin]+1)
        return -1 if combi[-1]==float('inf') else combi[-1]