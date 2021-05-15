# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 18:50:59 2021

@author: DELL
"""

from flask import Flask, request
import pandas as pd
#import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('clf.pkl', 'rb')
clf = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Hello World'

@app.route('/predict', methods = ['Get'])
def predict_note_authentication():
    
    """Let's Authenticate the Bank Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The Output Values
            
    """
    
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = clf.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return 'The Predicted value is ' + str(prediction)

@app.route('/predict_file', methods = ['POST'])
def predict_note_file():
    
    """Let's Authenticate teh Bank Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The Output values
    """
    
    df_test = pd.read_csv(request.files.get('file'))
    print(df_test.head())
    prediction = clf.predict(df_test)
    return 'The Predicted value for the csv is ' + str(list(prediction))


if __name__ == '__main__':
    app.run()
    
