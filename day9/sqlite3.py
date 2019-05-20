# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:51:22 2019

@author: Shivangi Sharma
"""

import os
import sqlite3
from pandas import DataFrame

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'db_university' )


# creating cursor
c = conn.cursor()

c.execute('drop table students')
# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE students(
          name  TEXT,
          age INTEGER,
          roll INTEGER,
          branch TEXT
          )""")


# STEP 2
c.execute("INSERT INTO students VALUES ('Sylvester', 34, 1,'CSE')")
c.execute("INSERT INTO students VALUES ('Sylvester', 34, 1,'CSE')")
c.execute("INSERT INTO students VALUES ('Sylvester', 34, 1,'CSE')")
c.execute("INSERT INTO students VALUES ('Sylvester', 34, 1,'CSE')")

c.execute("SELECT * FROM students")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM students")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["name","age","roll","branch"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()


