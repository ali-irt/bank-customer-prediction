# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UuToj5PbiOlL4poQeFesd3UpUKy02usq
"""

import numpy as np
import pandas as pd

"""CustomerId	Surname	CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Exited

"""

import keras

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import keras
# from keras.models import load_model
# 
# model = load_model('/content/BankExit.h5')
# import streamlit as st
# a=[0,0,0,0,0,0,0,0,0,0]
# credit = st.number_input('Credit Score')
# geo = st.number_input('0:france 1:spain 2:germany')
# gen = st.number_input('Gender 0 for female 1 for male')
# age = st.number_input('Age')
# ten = st.number_input('tenure')
# bal = st.number_input('Bal ance')
# prod = st.number_input('Products')
# card = st.number_input('Has card')
# act = st.number_input('Is active')
# sal = st.number_input('Salary')
# a[0]=credit
# a[1]=geo
# a[2]=gen
# a[3]=age
# a[4]=ten
# a[5]=bal
# a[6]=prod
# a[7]=card
# a[8]=act
# a[9]=sal
# 
# output = model.predict([0])
# st.write('output ',output)

!streamlit run /content/app.py &>/content/logs.txt&

!npx localtunnel --port 8501