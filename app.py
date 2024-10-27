import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

os.environ['GROQ_API_KEY'] = st.secrets['GROQ_API_KEY']

model = ChatGroq(model="llama3-8b-8192")

st.title("Autocorrect Tool")

para_to_be_corrected = st.text_area("Enter the paragraph to be corrected:")

if st.button("Correct Paragraph"):
    if para_to_be_corrected:
        messages = [
            SystemMessage(content="Act as an Autocorrect tool which corrects any spelling error or grammatical mistakes in the paragraph. Only return the corrected paragraph, no additional words or explanations."),
            HumanMessage(content=para_to_be_corrected),
        ]

        response = model.invoke(messages)

        st.write("### Corrected Paragraph:")
        st.write(response.content)
    else:
        st.warning("Please enter a paragraph to correct.")
