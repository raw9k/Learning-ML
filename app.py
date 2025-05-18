import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")
st.write("this is the simple text")

df = pd.DataFrame({
    "First column": [12,23,45,56,15,86],
    "Second column" : [46,49,63,17,59,73]
})

st.write("here is the dataframe")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(10,4), columns=["a","b",'c','d']
)

st.line_chart(chart_data)


name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}!!")
age = st.slider("Your age is", 0,100)
if age:
    st.write(f"your age is {age}")

options = ["cake", 'pizza','burger','drinks']
choice = st.selectbox("choose your menu", options)
st.write(f"You have selected {choice}")

upload = st.file_uploader("Choose a CSV file", type = 'csv')
if upload is not None:
    df = pd.read_csv(upload)
    st.write(df)