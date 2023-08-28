# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:12:27 2022

@author: HP
"""

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        
        if grades[i] < 38:
            continue
        elif (((grades[i]+1) % 5) == 0 or ((grades[i]+2) % 5) == 0):
            grades[i] = grades[i] + (5 -(grades[i] % 5)) 

    
    print (grades)



grades = [73, 67, 38, 33]
gradingStudents(grades)

