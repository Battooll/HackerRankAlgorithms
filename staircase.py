# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:34:11 2022

@author: HP
"""

def staircase(n):
    # Write your code here
    i = 1
    space = ' '
    while i < n+1:
        print (space*(n-i) + '#'*i)
        i = i + 1
    
n =6 
staircase(n)