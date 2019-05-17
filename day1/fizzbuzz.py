# -*- coding: utf-8 -*-
for i in range (0,101):
    if (i%3 and i%5):
        print ("fizzbuzz")
    elif(i%3):
        print("fizz")
    elif(i%5):
        print("buzz")
    else:
        print(i)
    
    