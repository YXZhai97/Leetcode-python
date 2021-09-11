# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:43:39 2021

@author: yixing 
"""

#some basic method to sort an array 

#1. 插入排序 insertion sort 

def insertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    print(array)
    return array

array=[1,25,8,2,5,33,10,0,25,100]
insertionSort(array)
    


#2. 冒泡排序

def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i): #最后i个已经排好了
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
    return arr

array=[1,25,8,2,5,33,10,0,25,100]
bubbleSort(array)


#3. Merge 排序(归并排序)








#4. 快速排序



