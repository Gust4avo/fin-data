import streamlit as st
import pandas as pd
import requests
import matplotlib.pylab as plt
import altair as alt

# Configurações da página
st.set_page_config(layout="centered", page_title="Média SELIC (API)")
st.title("Visualização da taxa Selic")

st.markdown("""
A tabela e o gráfico abaixo mostram a **média anual da taxa SELIC**,  
calculada a partir dos valores diários disponibilizados pela API do **Banco Central do Brasil**.  
Os dados estão sendo consumidos via **API FastAPI**. 
""")

try:
    resposta = requests.get("http://127.0.0.1:8000/selic/media-anual-json")
    resposta.raise_for_status()
    media_anual_dict = resposta.json()

    if resposta.status_code == 200:
        media_anual_dict = resposta.json()
        media_anual = pd.Series(media_anual_dict, name="Média SELIC")
        media_anual.index = media_anual.index.astype(int)

        st.subheader("📊 Média anual Selic (via API)")
        st.write(media_anual.round(2))

        st.subheader("📉 Gráfico da média anual (geral)")
        st.bar_chart(media_anual)

        # Prepara para gráfico interativo
        df_altair = media_anual.reset_index()
        df_altair.columns = ["ano", "valor"]

        st.subheader("📈 Gráfico Interativo")
        grafico = alt.Chart(df_altair).mark_bar(color="#64B5F6").encode(
            x=alt.X("ano:O", title="Ano"),
            y=alt.Y("valor:Q", title="Média Anual SELIC"),
            tooltip=["ano", "valor"]
        ).properties(width=600, height=400)
        st.altair_chart(grafico, use_container_width=True)

        # Botão de download
        csv = df_altair.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Baixar CSV",
            data=csv,
            file_name="media_anual_selic.csv",
            mime="text/csv"
        )
    
    else:
        st.error("Erro ao carregar dados da API.")

except Exception as e:
    st.error(f" Erro ao conectar com a API: {e}")
