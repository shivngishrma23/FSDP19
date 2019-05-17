# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:13:04 2019

@author: Shivangi Sharma
"""

str=input("name")
str1=(str[(str.find(" "))+1:]+" "+str[0:(str.find(" "))])
print (str1)