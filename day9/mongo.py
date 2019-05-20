# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:08:20 2019

@author: Shivangi Sharma
"""

import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://shivngi_23:shivangi@cluster0-shard-00-00-4tx7k.mongodb.net:27017,cluster0-shard-00-01-4tx7k.mongodb.net:27017,cluster0-shard-00-02-4tx7k.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.db_university

def add_employee(idd, first, last, pay):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.students.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.students.find()
    for i in user:
        print (i)




add_employee(1,'Sylvester', 'Fernandes', '50000')
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()