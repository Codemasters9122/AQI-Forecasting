import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load your pre-trained model (assuming it predicts PM2.5)
model = load_model('model.h5')

# Title of the web app
st.title("PM2.5 Concentration Prediction")

# Create sliders and input fields for each feature in the dataset
year = st.number_input('Year', min_value=2010, max_value=2024, value=2013, step=1)
month = st.slider('Month', min_value=1, max_value=12, value=1)
day = st.slider('Day', min_value=1, max_value=31, value=1)
hour = st.slider('Hour', min_value=0, max_value=23, value=0)

dewp = st.number_input('Dew Point (℃)', value=0.0, step=0.1)
temp = st.number_input('Temperature (℃)', value=20.0, step=0.1)
pres = st.number_input('Pressure (hPa)', value=1010.0, step=0.1)

# Only four wind directions available
cbwd = st.selectbox('Combined Wind Direction', ['NE', 'NW', 'SE', 'SW'])
iws = st.number_input('Cumulated Wind Speed (m/s)', value=0.0, step=0.1)
is_snow = st.number_input('Cumulated Hours of Snow', value=0.0, step=0.1)
ir_rain = st.number_input('Cumulated Hours of Rain', value=0.0, step=0.1)

# Map wind direction to numerical values (optional, based on how your model handles it)
wind_directions = {'NE': 0, 'NW': 1, 'SE': 2, 'SW': 3}
cbwd_encoded = wind_directions[cbwd]

# Create an input array from the user input
input_data = np.array([[year, month, day, hour, dewp, temp, pres, cbwd_encoded, iws, is_snow, ir_rain]])

# When the user clicks the 'Predict' button
if st.button('Predict PM2.5'):
    prediction = model.predict(input_data)
    st.write(f"Predicted PM2.5 concentration: {prediction[0][0]:.2f} µg/m³")
