# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:09:41 2019

@author: Shivangi Sharma
"""
def days_in_month(month):
    month=input("enter month name")
    month= month.lower
    list1=['january','february','march','april','may','june','july','august','september','october','november','december']
    list2=[31,28,31,30,31,20,31,31,30,31,30,31]
    index=list1.index(month)
    return list2(index)
                
            
    
    
    
