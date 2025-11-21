# Create a webpage using streamlit
# get the name, weight, height from the user
# When user clicks on the button, calculate the BMI and display it on the webpage

# bmi = weight / height^2

import streamlit

import seaborn

from matplotlib import pyplot

streamlit.header("BMI Calculation")

name = streamlit.text_input("Enter your name: ")

weight = streamlit.number_input("Enter your weight: ")

height = streamlit.number_input("Enter your height: ")

if streamlit.button("Calculate BMI"):

    bmi = weight / (height ** 2)

    streamlit.success(f"Hi {name}, your BMI is {bmi}")