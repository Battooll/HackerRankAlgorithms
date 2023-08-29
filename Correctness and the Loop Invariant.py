# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:50:29 2023

@author: HP
"""

def insertion_sort(arr):
    # Write your code here
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    print(*arr)
                
arr=[7,1,6,3,4,5,2]
insertion_sort(arr)