# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 02:04:30 2022

@author: HP
"""

from datetime import datetime


def diagonalDifference(arr):
    temp = 0
    emp = 0
    for i in range(0,len(arr)):
        temp = temp + arr[i][i]
    
    for j in range(0,len(arr)):
        emp = emp + arr[j][len(arr)-1-j]
    
    return abs(temp - emp)

start = datetime.now()
# some kind of code

arr = [[11,2,4],[4,5,6],[10,8,-12]]   

print (diagonalDifference(arr))

print(datetime.now() - start)