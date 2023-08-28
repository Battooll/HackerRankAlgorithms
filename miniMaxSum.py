# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 22:38:24 2022

@author: HP
"""

def miniMaxSum(arr):
    # Write your code here
    """min = float('inf')
    max = 0
    sum = 0
    for i in range(1,len(arr)):
        sum = sum + arr[i]
    if sum <= min:
        min = sum
    if sum >= max:
        max = sum
    
    sum = 0
    for i in range(0,len(arr)):
        if i!=1:    
            sum = sum + arr[i]
    if sum <= min:
            min = sum
    if sum >= max:
            max = sum
    
    sum = 0
    for i in range(0,len(arr)):
        if i!=2:    
            sum = sum + arr[i]
    if sum <= min:
            min = sum
    if sum >= max:
            max = sum

    sum = 0
    for i in range(0,len(arr)):
        if i!=3:    
            sum = sum + arr[i]
    if sum <= min:
            min = sum
    if sum >= max:
            max = sum
            
    sum = 0
    for i in range(0,len(arr)-1):
         
        sum = sum + arr[i]
    if sum <= min:
                min = sum
    if sum >= max:
                max = sum
                
    print (min, " ", max)
    
    """
    sor = sorted(arr)
    print (sum(sor[:4]), sum(sor[1:]))
    
    
miniMaxSum([5, 4, 3, 2, 1])