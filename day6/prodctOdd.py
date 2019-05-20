# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:02:24 2019

@author: Shivangi Sharma
"""
list1=reduce(lambda x,y:x*y,(filter(lambda x:x%2==1,map(int,input("enter number").split('.')))))