import streamlit as st
import requests

st.title("Persona Adaptive Customer Support")

message = st.text_input("Ask your question")

if st.button("Send"):
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        params={"question": message}
    )

    st.write(response.json())