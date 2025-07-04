import streamlit as st

def initialize_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    return st.session_state.chat_history

def update_memory(role, message):
    st.session_state.chat_history.append({"role": role, "message": message})