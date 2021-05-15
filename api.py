# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:02:47 2021

@author: DELL
"""


import pandas as pd
import pickle
import streamlit as st
from PIL import Image

pickle_in = open('clf.pkl', 'rb')
clf = pickle.load(pickle_in)


#@app.route('/')
def welcome():
    return 'Hello World'

#@app.route('/predict', methods = ['Get'])
def predict_note_authentication(variance, skewness, curtosis, entropy):
    
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
    
    prediction = clf.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction

def main():
    st.title('Bank Authenticator')
    html_temp = """
    <div style = 'background-color:blue; padding:10px'>
    <h2 style = 'color:white; text-align:center;'>BANK AUTHENTICATION APP</h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input('Variance')
    skewness = st.text_input('Skewness')
    curtosis = st.text_input('Curtosis')
    entropy = st.text_input('Entropy')
    result=""
    if st.button('Predict'):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
    st.success('The Output is {}'.format(result))
    if st.button('About'):
        st.text('Lets Predict')
        st.text('Build with Passion')

if __name__ == '__main__':
    main()
    