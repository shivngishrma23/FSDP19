# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:34:02 2019

@author: Shivangi Sharma
"""
import random
names=['mary','isla','sam']
codes_names=['mr.pink','mr.orange','mr.blonde']
map_iterator=map(lambda x:random.choice(codes_names),names)
print(list(map_iterator))