import streamlit as st
from llama_cpp import Llama

# Load model hanya sekali
@st.cache_resource
def load_model():
    return Llama(model_path="model.gguf")

llm = load_model()

st.title("🦙 Chatbot Lokal dengan LLaMA.cpp")

# Chat interface
user_input = st.text_input("Ketik pertanyaanmu:")
if user_input:
    output = llm(user_input, max_tokens=200)
    response = output["choices"][0]["text"]
    st.markdown(f"**Bot:** {response}")
