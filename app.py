import streamlit as st
from Model import Model

# Initialize model once
model = Model()

# Set page title
st.set_page_config(page_title="Python Code Comment Generator", page_icon="💬")
st.title("Python Code Comment Generator")

# Input Text Area
code_input = st.text_area("Paste your Python code below:", height=300)

# Button to generate
if st.button("Generate Comments"):
    if code_input.strip() == "":
        st.warning("Please paste some code first!")
    else:
        try:
            response = model.ask(code_input)
            st.success("Comments generated successfully!")
            st.text_area("Generated Code with Comments:", value="\n".join(response), height=300)
        except Exception as e:
            st.error(f"An error occurred: {e}")
