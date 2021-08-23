# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:56:02 2021

@author: yixin
"""

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]
  
# using zip() to map values
mapped = zip(name, roll_no, marks)
  
# converting values to print as set
mapped = set(mapped)
  
# printing resultant values 
print ("The zipped result is : ",end="")
print (mapped)

b=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12]]
z=zip(*b)
print(list(z))