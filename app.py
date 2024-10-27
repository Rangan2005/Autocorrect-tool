import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Setting up the API key securely
os.environ['GROQ_API_KEY'] = st.secrets['GROQ_API_KEY']

# Initialize the ChatGroq model
model = ChatGroq(model="llama3-8b-8192")

# Streamlit app setup
st.title("Autocorrect Tool")

# User input
para_to_be_corrected = st.text_area("Enter the paragraph to be corrected:")

# Check if input is provided and button is pressed
if st.button("Correct Paragraph"):
    if para_to_be_corrected:
        # Create messages for LangChain model
        messages = [
            SystemMessage(content="Act as an Autocorrect tool which corrects any spelling error or grammatical mistakes in the paragraph. Only return the corrected paragraph, no additional words or explanations."),
            HumanMessage(content=para_to_be_corrected),
        ]

        # Get response from model
        response = model.invoke(messages)
        
        # Display corrected text
        st.write("### Corrected Paragraph:")
        st.write(response.content)
    else:
        st.warning("Please enter a paragraph to correct.")
