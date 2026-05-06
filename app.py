import streamlit as st
from rag import get_response

st.title("AI Resume RAG System")

query = st.text_input("Ask a question about the resume")

submit = st.button("Submit")

if submit and query:
    response = get_response(query)

    st.write(response)