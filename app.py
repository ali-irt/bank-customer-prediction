import numpy as np
import streamlit as st
import keras
from keras.models import load_model

# Load the trained model
model = load_model('model.h5')  # Ensure you have saved your Keras model as 'model.h5'

# Initialize list for inputs
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Streamlit input fields
credit = st.number_input('Credit Score')
geo = st.number_input('Geography (0: France, 1: Spain, 2: Germany)')
gen = st.number_input('Gender (0: Female, 1: Male)')
age = st.number_input('Age')
ten = st.number_input('Tenure')
bal = st.number_input('Balance')
prod = st.number_input('Number of Products')
card = st.number_input('Has Card (0: No, 1: Yes)')
act = st.number_input('Is Active Member (0: No, 1: Yes)')
sal = st.number_input('Estimated Salary')

# Store user input in the array 'a'
a[0] = credit
a[1] = geo
a[2] = gen
a[3] = age
a[4] = ten
a[5] = bal
a[6] = prod
a[7] = card
a[8] = act
a[9] = sal

# Convert input to numpy array and reshape for model
input_data = np.array([a])  # Reshape input to match model input format

# Make a prediction
if st.button('Predict'):  # Add a button to trigger prediction
    output = model.predict(input_data)
    st.write('Output:', output)
