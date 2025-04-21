import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os


st.set_page_config(
    page_title="Comparativo SELIC x IPCA x CDI",
    layout="centered"
)

# === Caminhos seguros para os arquivos ===
CAMINHO_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
CAMINHO_SELIC = os.path.join(CAMINHO_BASE, "etl/dados/selic_media_anual.csv")
CAMINHO_IPCA = os.path.join(CAMINHO_BASE, "etl/dados/ipca_anual.csv")
CAMINHO_CDI = os.path.join(CAMINHO_BASE, "etl/dados/cdi_media_anual.csv")

# === Título da página ===
st.title("Comparativo: SELIC x Inflação (IPCA) x CDI")


df_selic = pd.read_csv(CAMINHO_SELIC)
df_ipca = pd.read_csv(CAMINHO_IPCA)
df_cdi = pd.read_csv(CAMINHO_CDI)



# Fazendo merge para alinhar os dados
df_merged = df_selic.merge(df_ipca, on="ano", how="inner")
df_merged = df_merged.merge(df_cdi, on="ano", how="inner")


anos = df_merged["ano"]
selic = df_merged["media_selic"]
ipca = df_merged["valor"]
cdi = df_merged["media_cdi"]

# === Seleção pelo usuário ===
opcoes = st.multiselect(
    "Escolha os indicadores para comparar com a SELIC:",
    ["Inflação (IPCA)", "CDI"]
)

# === Gerar o gráfico ===
fig, ax = plt.subplots()

# Linha da SELIC
ax.plot(anos, selic, label="SELIC", color="blue", linewidth=2, marker="o")

# Linha da IPCA se escolhida
if "Inflação (IPCA)" in opcoes:
    ax.plot(anos, ipca, label="Inflação (IPCA)", color="orange", linewidth=2, marker="s")

# Linha do CDI se escolhida
if "CDI" in opcoes:
    ax.plot(anos, cdi, label="CDI", color="green", linewidth=2, marker="^")

# Ajustes visuais
ax.set_title("Comparativo Anual", fontsize=16)
ax.set_xlabel("Ano")
ax.set_ylabel("Taxa (%)")
ax.legend()
ax.grid(True)

# Exibir no Streamlit
st.pyplot(fig)
