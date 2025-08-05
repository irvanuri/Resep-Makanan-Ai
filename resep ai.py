import streamlit as st
import google.generativeai as genai

# Masukkan API key kamu
API_KEY = "AIzaSyCe1FaZ4py5e3i7lTBTjygATXA0xmyl8IY"
genai.configure(api_key=API_KEY)

import google.generativeai as genai

def get_recipe(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    response = model.generate_content([prompt])
    return response.text


st.title("Cari Resep Makanan dengan Gemini AI")

user_input = st.text_input("Masukkan bahan makanan atau nama resep:")

if st.button("Cari Resep"):
    if user_input:
        with st.spinner("Mencari resep..."):
            hasil = get_recipe(f"Berikan saya resep makanan dengan bahan {user_input}")
            st.success("Berhasil ditemukan!")
            st.write(hasil)
    else:
        st.warning("Silakan masukkan kata kunci dulu.")


