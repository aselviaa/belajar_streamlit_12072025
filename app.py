import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.title("This is a title 🤩")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
