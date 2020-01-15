# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 02:01:02 2020

@author: dell
"""

from flask import Flask
import graph # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return graph.draw()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)