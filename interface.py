import streamlit as st
from main import fzr_qrcode

st.markdown("""
    <h1 class="titulo">QRCodex</h1> 
    <style>
    .titulo{
        text-align: center;
        color: black;
        text-shadow: 2px 2px 5px grey;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <h2 class="texto">Insira o Link abaixo para que possa ser criado o seu QRCode 👍🏻</h2> 
    <style>
    .texto {
        text-align: center;
        color: black;
        text-shadow: 2px 2px 5px grey;
        margin-top: 40px;
        font-size: 25px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .stDownloadButton {
        display: flex;
        justify-content: center;
    }
    .stDownloadButton > button {
        color: white;
        background-color: black;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

input_text = st.text_input("")

if input_text:
    try:
        img_bytes = fzr_qrcode(input_text)
        st.download_button(
            label="Download QRCode",
            data=img_bytes,
            file_name="QRCode.png",
            mime="png"
        )
    except Exception as e:
        st.error(f"Erro ao processar o vídeo: {e}")
