import streamlit as st
import requests

st.title("Persona Support Agent")

question = st.text_input(
    "Ask a question"
)

if st.button("Submit"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        params={
            "question": question
        }
    )

    st.json(response.json())