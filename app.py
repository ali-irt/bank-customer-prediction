import numpy as np
import streamlit as st
from keras.models import load_model

# Load the trained model
model = load_model('BankExit.h5')  # Ensure your Keras model is saved as 'model.h5'

# Streamlit input fields
st.title("Customer Prediction Model")

credit = st.number_input('Credit Score', min_value=0, max_value=1000)
geo = st.selectbox('Geography', options=[0, 1, 2], format_func=lambda x: ['France', 'Spain', 'Germany'][x])
gen = st.selectbox('Gender', options=[0, 1], format_func=lambda x: ['Female', 'Male'][x])
age = st.number_input('Age', min_value=18, max_value=100)
ten = st.number_input('Tenure', min_value=0, max_value=10)
bal = st.number_input('Balance', min_value=0.0)
prod = st.number_input('Number of Products', min_value=1, max_value=4)
card = st.selectbox('Has Credit Card', options=[0, 1], format_func=lambda x: ['No', 'Yes'][x])
act = st.selectbox('Is Active Member', options=[0, 1], format_func=lambda x: ['No', 'Yes'][x])
sal = st.number_input('Estimated Salary', min_value=0.0)

# Collect user inputs into the array 'a'
a = [credit, geo, gen, age, ten, bal, prod, card, act, sal]

# Convert input to numpy array and reshape for model (1, 10) for one instance
input_data = np.array([a])

# Make a prediction when 'Predict' button is clicked
if st.button('Predict'):
    try:
        # Perform prediction
        output = model.predict(input_data)

        # Display the prediction
        st.write(f'Prediction Output: {output}')
        
        # If it's a classification model, you may want to interpret the output
        # Example for binary classification: assume output is a probability
        if output.shape[-1] == 1:
            prediction = (output > 0.5).astype(int)
            st.write(f'Predicted Class: {"Yes" if prediction[0] == 1 else "No"}')

    except Exception as e:
        st.error(f"An error occurred: {e}")
