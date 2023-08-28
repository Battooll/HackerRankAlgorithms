# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 23:44:14 2022

@author: HP
"""

def timeConversion(s):
    # Write your code here
    
    if s[-2:] == "AM" and s[:2] == "12":
        print ("00" + s[2:-2])
    elif "AM" in s:
        print (s[:len(s)-2])
    elif s[-2:] == "PM" and s[:2] == "12":
        print (s[:-2])
    else: 
        x = str(int(s[:2]) + 12)
        
    
        print (x + s[2:-2])


s ="07:05:45PM"
timeConversion (s)

#print (int(s[:2]))