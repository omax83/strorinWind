#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
