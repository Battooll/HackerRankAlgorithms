# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:23:55 2022

@author: HP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zeroes = 0
    pos = 0
    neg = 0
    for i in range(0,len(arr)):
        if arr[i] == 0:
           zeroes = zeroes + 1
        elif arr[i] > 0:
            pos = pos + 1 
        else:
            neg = neg + 1
            
    print ( (pos/len(arr)) )
    print ( (neg/len(arr)) )
    print ( (zeroes/len(arr)) )
    
    
    
arr = [-4 ,3 ,-9 ,0 ,4 ,1]

plusMinus(arr)