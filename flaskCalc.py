#!/bin/pyhton3

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')

app.run(host='0.0.0.0', port=5000, debug=True)