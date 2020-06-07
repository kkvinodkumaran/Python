#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:04:26 2020

@author: vinodkariyathungalkumaran
"""

import pymongo


def initFunction():
    print("Test")
class MyMongo:
    
    def saveToMongo():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]

        mylist = [
        { "name": "Vinod", "address": "PayneAve"},
        { "name": "Ahmed", "address": "Sunnyvale"},        
        ]

        x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
        print(x.inserted_ids)

        for x in mycol.find():
            print(x)
  
