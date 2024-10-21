from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World :)"
