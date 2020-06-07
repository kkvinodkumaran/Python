#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:40:21 2020

@author: vinodkariyathungalkumaran
"""

import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root@123"
)
mycursor = mydb.cursor()
with open('/Users/vinodkariyathungalkumaran/Documents/E_Drive/Mypython/employee.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
   
        name=row[0]
        address=row[1]
        department=row[2]
        sql = "INSERT INTO person.employee (name, address,department) VALUES (%s, %s,%s)"
        val = (name, address,department)
        mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


print(mydb)

mycursor.execute("SELECT * FROM person.employee")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

