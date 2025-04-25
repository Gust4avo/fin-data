import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(layout="centered", page_title="Média SELIC")
st.title("Visualização da taxa Selic")
st.markdown("""
A tabela e o gráfico abaixo mostram a **média anual da taxa SELIC**,  
calculada a partir dos valores diários disponibilizados pela API do **Banco Central do Brasil**.  
Você pode filtrar os anos desejados ou baixar os dados em CSV.  
""")

df = pd.read_csv("etl/dados/selic_limpo.csv")
df["data"] = pd.to_datetime(df["data"])
df["ano"] = df["data"].dt.year

media_anual = df.groupby("ano")["valor"].mean()

# Exibição da média geral
st.subheader("📊 Média anual Selic (geral)")
st.write(media_anual.round(2))

# Gráfico simples da média geral
st.subheader("📉 Gráfico da média anual (geral)")
st.bar_chart(media_anual)

# Seletor de anos - só aparece aqui embaixo
st.subheader("🔍 Filtrar anos para visualização detalhada")
anos_disponiveis = df['ano'].unique()
anos_selecionados = st.multiselect(
    "Selecione os anos para exibir:",
    options=sorted(anos_disponiveis),
    default=sorted(anos_disponiveis)
)

# Aplica o filtro com base no que o usuário selecionou
df_filtrado = df[df['ano'].isin(anos_selecionados)]

# Gráfico interativo
st.subheader("📈 Gráfico Interativo da Média Anual")
st.dataframe(df_filtrado, use_container_width=True)

grafico = alt.Chart(df_filtrado).mark_bar(color="#64B5F6").encode(
    x=alt.X("ano:O", title="Ano"),
    y=alt.Y("valor:Q", title="Média Anual SELIC"),
    tooltip=["ano", "valor"]
).properties(
    width=600,
    height=400
)
st.altair_chart(grafico, use_container_width=True)

# Botão para baixar CSV
csv = df_filtrado.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Baixar CSV",
    data=csv,
    file_name="media_anual_selic.csv",
    mime="text/csv"
)
