# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 19:11:07 2021

@author: DELL
"""
from flask import Flask, request
import pandas as pd
#import numpy as np
import pickle

app = Flask(__name__)

pickle_in = open('models/clf.pkl', 'rb')
clf = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Hello World'

@app.route('/predict')
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = clf.predict([[variance, skewness, curtosis, entropy]])
    return 'The Predicted value is ' + str(prediction)

@app.route('/predict_file', methods =['POST'])
def predict_note_file():
    df_test = pd.read_csv(request.files.get('file'))
    prediction = clf.predict(df_test)
    return 'The Predicted value for the csv is ' + str(list(prediction))


if __name__ == '__main__':
    app.run()
    
