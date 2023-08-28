# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:49:41 2022

@author: HP
"""

def migratoryBirds(arr):
    # Write your code here
    """max = 0
    res = 0
    for i in range(len(arr)):
        x= arr.count(arr[i])
        if x > max:
            max = x
            res = arr[i]
    return res"""

    """ Make a set of the list so that the duplicate elements are deleted. Then find the highest count of occurrences of each element in the set and thus, we find the maximum out of it. """
    
    return max(set(arr), key = arr.count)


print (migratoryBirds([1,2,3,1,1,2,2,2,2,3,4,5,4,5]))