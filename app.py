import streamlit as st
from main import run_cdss_pipeline
from rag_utils import embed_pdf_to_faiss
from chat_memory import initialize_memory, update_memory

st.set_page_config(page_title="CDSS Chatbot", layout="centered")
st.title("🧠 Clinical Decision Support System")

chat_history = initialize_memory()
index_path = "faiss_index"

with st.sidebar:
    st.header("📄 Upload STG PDF")
    uploaded_file = st.file_uploader("Upload Gujarat STG PDF", type=["pdf"])
    if uploaded_file:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        embed_pdf_to_faiss("temp.pdf", index_path)
        st.success("✅ STG embedded successfully!")

st.markdown("### 💬 Chat")
for chat in chat_history:
    st.chat_message(chat["role"]).markdown(chat["message"])

prompt = st.chat_input("Type symptoms...")
if prompt:
    update_memory("user", prompt)
    with st.spinner("Processing..."):
        output = run_cdss_pipeline(prompt, index_path)
        response = f"**History:** {output['History']}\n\n**Diagnosis:** {output['Diagnosis']}\n\n**Treatment:** {output['Treatment']}"
    update_memory("assistant", response)
    st.rerun()
