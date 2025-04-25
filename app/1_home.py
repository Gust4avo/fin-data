# app/streamlit_dashboard.py
import streamlit as st

st.set_page_config(page_title=" FinData ", layout="centered")
st.title("Bem-vindo ao FinData")
st.markdown("""
Aqui você pode visualizar e comparar três importantes indicadores financeiros do Brasil:

- **SELIC**: taxa básica de juros do país
- **IPCA**: índice oficial de inflação
- **CDI**: taxa média do mercado interbancário
            
""")

st.sidebar.title("Navegação")
st.sidebar.success("Selecione uma página acima.")


