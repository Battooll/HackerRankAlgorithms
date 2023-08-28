# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:50:07 2022

@author: HP
"""
from datetime import datetime
def diagonalDifference(arr):
    # Write your code here
    # [[1,2,3],[4,5,6],[9,8,9]]
    l_diagonal = 0
    r_diagonal = 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i==j and (i+j) == (len(arr) - 1):
                l_diagonal += arr[i][j]
                r_diagonal += arr[i][j]
            elif i==j:
                l_diagonal += arr[i][j]
            elif (i+j) == (len(arr) - 1):
                r_diagonal += arr[i][j]
    return abs(l_diagonal - r_diagonal)

start = datetime.now()
# some kind of code

arr = [[11,2,4],[4,5,6],[10,8,-12]]   

print (diagonalDifference(arr))

print(datetime.now() - start)
# [0,0] [1,1] [2,2]
# [0,2]  [1,1]  [2,0]

#[0, 2, 4]
#[2, 2, 2]


# [0,0] [1,1] [2,2] [3,3]
# [0,3]  [1,2]  [2,1] [3,0]


#[0, 2, 4, 6]
#[3, 3, 3, 3]

