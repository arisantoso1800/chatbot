import streamlit as st
import os
import gdown
from llama_cpp import Llama

# Cek dan unduh file model jika belum ada
MODEL_PATH = "model.gguf"
if not os.path.exists(MODEL_PATH):
    FILE_ID = "14vVS2SSAEartUIJfLwX8rL3r0gWVnE9d"  # ganti dengan file ID Drive kamu
    gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", MODEL_PATH, quiet=False)

# Muat model (cache untuk efisiensi)
@st.cache_resource
def load_model():
    return Llama(model_path=MODEL_PATH)

llm = load_model()

st.title("🦙 Chatbot Lokal dengan LLaMA.cpp")

user_input = st.text_input("Ketik pertanyaanmu:")
if user_input:
    output = llm(user_input, max_tokens=200)
    response = output["choices"][0]["text"]
    st.markdown(f"**Bot:** {response}")
