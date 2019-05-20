# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:35:58 2019

@author: Shivangi Sharma
"""
list1= input("enter number ").split(" ")
positive=[]
print("list1")

for item in list1:
    if((int(item)>0) and (item==item[:-1])):
        positive.append("true")
    else:
        positive.append("false")
print(all(positive))
        
