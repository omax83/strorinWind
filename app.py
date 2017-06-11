# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
from settings import *
import vk

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/', methods=['POST'])
def processing():
  return '13507e18'
