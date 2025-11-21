import streamlit

# streamlit
#=======================

# Used to convert the python code, ml projects into a web application.

# ipynb X
# use py files


streamlit.header("Addition of two numbers")

num1 = streamlit.number_input("Enter first number: ")

num2 = streamlit.number_input("Enter second number: ")

if streamlit.button("Add"):

    result1 = num1 + num2

    streamlit.success(f"The total is {result1}")

elif streamlit.button("Subtract"):

    result2 = num1 - num2

    streamlit.success(f"The difference is {result2}")