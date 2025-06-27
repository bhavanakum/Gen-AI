import streamlit as st
from Langchain_helper import ChatGoogleGen

# Page configuration
st.set_page_config(page_title="ATLIQ Database Q&A", page_icon="📊", layout="centered")

# Custom title
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>📊 ATLIQ DATABASE - Natural Language Q&A</h1>", unsafe_allow_html=True)

# Input section
st.markdown("#### 🤖 Ask a question about the `t_shirts` database:")
question = st.text_input("Enter your question here", placeholder="e.g. How many white Nike t-shirts are available in size M?")

if st.button("Get Answer"):
    if not question.strip():
        st.warning("⚠️ Please enter a question before submitting.")
    else:
        with st.spinner("Generating answer..."):
            answer = ChatGoogleGen(question)

        st.success("✅ Answer generated!")
        st.markdown("### 📝 Answer:")
        st.markdown(f"**{answer}**")