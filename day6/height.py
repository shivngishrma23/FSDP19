# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:03:55 2019

@author: Shivangi Sharma
"""

from functools import reduce
people=[{'name' : 'mary','height' : 160},
        {'name' : 'isla','height' : 80},
        {'name' : 'sam'}]
heightpeople=list(filter(lambda x:'height' in x,people))
if len(heightpeople)>0:
    totalheight=reduce(lambda a,x:a["height"]+x['height'],heightpeople)
    average= totalheight/len(heightpeople)
    print ('average')
