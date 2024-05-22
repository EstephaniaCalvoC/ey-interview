import time
import streamlit as st
from langserve import RemoteRunnable


st.set_page_config(page_title="EY Chatbot Demo", page_icon=":robot:")
st.header("EY Chatbot Demo")


if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = RemoteRunnable("http://localhost:8000/rag")   
    
    
if "messages" not in st.session_state:
    st.session_state.messages = []
   
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What can I help you with?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        response = st.session_state.rag_chain.invoke({"input": prompt})
        st.markdown(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})
        