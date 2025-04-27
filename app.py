import streamlit as st
from Model import Model

# Initialize model
model = Model()

# Streamlit page settings
st.set_page_config(page_title="Python Code Comment Generator", layout="wide")

# Sidebar
st.sidebar.title("Settings")
st.sidebar.info("This app uses **Groq's LLaMA 3** model to generate comments for your Python code!")

# Select comment detail level
comment_level = st.sidebar.selectbox(
    "Select Comment Detail Level:",
    ("Beginner (Explain everything)", "Intermediate (Moderate explanations)", "Minimal (Quick clarifications)")
)

# Main Title
st.title("Python Code Comment Generator")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Your Code")
    code_input = st.text_area("Paste your Python code here", height=400, label_visibility="collapsed")

    generate = st.button("Generate Comments")  # <-- Moved here!

with col2:
    st.subheader("Generated Comments")

    if generate:
        if not code_input.strip():
            st.warning("Please paste some code first!")
        else:
            with st.spinner("Generating comments... please wait ✨"):
                try:
                    response = model.ask(code_input, comment_level)
                    commented_code = "\n".join(response)
                    st.text_area("Commented Code:", value=commented_code, height=400, label_visibility="collapsed")
                    st.success("Comments generated successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    else:
        st.text_area("Commented Code:", value="", height=400, label_visibility="collapsed")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>Made with ❤️ using Streamlit and LLaMA 3</div>",
    unsafe_allow_html=True
)
