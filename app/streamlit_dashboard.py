import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="centered", page_title="Média SELIC (API)")
st.title("Visualização da taxa Selic via API")

st.markdown("""
Os dados abaixo foram obtidos da **API FastAPI local** do projeto.  
""")

resposta = requests.get("http://127.0.0.1:8000/selic/media-anual-json")

if resposta.status_code == 200:
    media_anual_dict = resposta.json()
    media_anual = pd.Series(media_anual_dict)
    media_anual.index = media_anual.index.astype(int)

    st.subheader("📊 Média anual Selic (via API)")
    st.write(media_anual)

    st.subheader("📉 Gráfico da média anual (via API)")
    st.bar_chart(media_anual)
else:
    st.error("Erro ao carregar dados da API.")
