# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:42:21 2022

@author: HP
"""

import numpy as np

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    res = 0
    """temp = list(np.array_split(s, m+1))
    
    for i in range(len(temp)):
        if sum(temp[i]) == d:
            res += 1
    """
    for i in range(len(s)):
        if m>1:
            temp = s[i]
            for j in range (i+1,m):
                temp += s[j] 
            if temp == d:
                res += 1
        if m==1:
            if s[i] == d:
                res += 1
        
                
    return (res) 


s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]  
d= 18
m = 7
print (birthday(s, d, m))


#temp = list(np.array_split(s, len(s)/m +1 ))


#print (temp)