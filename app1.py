import pandas as pd
import numpy as np
from scipy import optimize
import streamlit as st


st.set_page_config(page_title="Calculator", page_icon=":calculator:", layout="wide")


st.title("電卓")

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

num1 = st.number_input("Enter first number:")
operator = st.selectbox("Select operator:", ["+", "-", "*", "/"])
num2 = st.number_input("Enter second number:")

if st.button("="):
    result = calculate(num1, operator, num2)
    st.success("Result: {}".format(result))

if st.button("="):
    result = calculate(num1, operator, num2)
    st.success("Result: {}".format(result))
