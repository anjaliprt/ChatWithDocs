# Save as streamlit_app.py
import streamlit as st
from main import rag_chain

st.set_page_config(page_title=" ChatWithDocs", page_icon="🗨️", layout="centered")
st.title("🗨️ ChatWithDocs")
st.markdown("Ask any question about your documents")

query = st.text_input("🔍 Your question:")
if st.button("Ask"):
    with st.spinner("Thinking..."):
        response = rag_chain.invoke(query)
    st.write("🤖 **Answer:**")
    st.success(response.content)
