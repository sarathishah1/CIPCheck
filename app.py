from flask import Flask
import pandas as pd
from helper_function import create_base_encoding 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World :)"

@app.route("/cipcheck",methods=['POST'])
def search_duplicate():
    query = request.json.get('query')
    baseencoding=create_base_encoding()
    results=generate_output(create_input_encoding(x),df['Intermediate Description'].tolist())
    return "Hello World"
    
