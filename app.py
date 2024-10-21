from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World :)"

@app.route("/cipcheck",methods=['POST'])
def search_duplicate():
    baseencoding=create_base_encoding()
    return "Hello World"
    
