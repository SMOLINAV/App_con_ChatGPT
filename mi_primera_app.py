# app_streamlit.py

import streamlit as st

# Título
st.title("Mi primera app")

# Autor
st.write("Esta app fue elaborada por Santiago M")

# Pregunta al usuario su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Imprimir mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")

