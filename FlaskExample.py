#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:28:21 2020

@author: vinodkariyathungalkumaran
"""

import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>This is my first flask python program.</p>"


@app.route("/posttest", methods=['GET', 'POST'])
def notes_list():
    if request.method == 'POST':
           content = request.json
           print(content['name'])
           return content
    request.method == 'GET'
    return "GET RESPONSE"


app.run()
