# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:45:18 2018

@author: 
- more codes will be added 
output:
Print all the months name of year: 
January
February
March
April
May
June
July
August
September
October
November
December
Cool !

"""
import calendar
print("Print all the months name of year: ")
for month_number in range(1,13):
    x = calendar.month_name[month_number]
    print(x)

print("Cool !")
