import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.title("This is a title 🤩")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")
st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.area_chart(chart_data, x="col1", y="col2", color="col3")
