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
