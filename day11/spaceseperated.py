# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:02:08 2019

@author: Shivangi Sharma
"""
import numpy as np


uinput = input("enter nine numbers : ").split(" ")

uinput = np.array(uinput)
uinput = uinput.reshape(3,3)
print(uinput)