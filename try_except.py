# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:22:33 2021

@author: yixing
"""

try:
    123
    number=int(input("enter a number: ")) #input error
    print(number)
    if number==1:
        number=number/0
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid Input")