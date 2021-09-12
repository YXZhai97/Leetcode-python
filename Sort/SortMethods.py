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


def mergeSort(arr):
    
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]
        
    #recursion 
        mergeSort(left_arr)
        mergeSort(right_arr)
    
    
    #merge 
        i=0
        j=0
        k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
        
            k+=1
        
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1
    
    return arr 


array=[1,25,8,2,5,33,10,0,25,100]
print(mergeSort(array) )





#4. 快速排序



