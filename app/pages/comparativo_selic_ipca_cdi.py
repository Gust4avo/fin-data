import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

st.set_page_config(page_title=" FinData ", layout="centered")
st.title("Bem-vindo ao FinData")
st.markdown("""
Bem-vindo ao **Fin-Data**!  
Aqui você pode visualizar e comparar três importantes indicadores financeiros do Brasil:

- **SELIC**: taxa básica de juros do país
- **IPCA**: índice oficial de inflação
- **CDI**: taxa média do mercado interbancário
            
""")

# === Caminhos seguros para os arquivos ===
CAMINHO_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
CAMINHO_SELIC = os.path.join(CAMINHO_BASE, "etl/dados/selic_media_anual.csv")
CAMINHO_IPCA = os.path.join(CAMINHO_BASE, "etl/dados/ipca_anual.csv")
CAMINHO_CDI = os.path.join(CAMINHO_BASE, "etl/dados/cdi_media_anual.csv")

# === Título a página ===
st.title("Comparativo Anual - SELIC, IPCA e CDI (2020–2025)")

# === Leitura dos dados ===
df_selic = pd.read_csv(CAMINHO_SELIC)
df_ipca = pd.read_csv(CAMINHO_IPCA)
df_cdi = pd.read_csv(CAMINHO_CDI)

# === Merge para alinhar os anos entre os três DataFrames ===
df_merged = df_selic.merge(df_ipca, on="ano", how="inner")
df_merged = df_merged.merge(df_cdi, on="ano", how="inner")

# === Preparação dos dados ===
anos = df_merged["ano"]
selic = df_merged["media_selic"] 
ipca = df_merged["valor"]           
cdi = df_merged["media_cdi"]       

# === Seletor interativo dos indicadores ===
opcoes = st.multiselect(
    "Escolha os indicadores para comparar com a SELIC:",
    ["Inflação (IPCA)", "CDI"],
    default=["Inflação (IPCA)", "CDI"]
)

# === Criação do gráfico ===
fig, ax = plt.subplots(figsize=(10, 6))

# Linha da SELIC
ax.plot(anos, selic, label="SELIC", color="blue", linewidth=2, marker="o")

# Linha da IPCA se selecionada
if "Inflação (IPCA)" in opcoes:
    ax.plot(anos, ipca, label="Inflação (IPCA)", color="red", linewidth=2, marker="s")

# Linha do CDI se selecionado
if "CDI" in opcoes:
    ax.plot(anos, cdi, label="CDI", color="green", linewidth=2, marker="^")

# === Personalização do gráfico ===
ax.set_title("Comparativo Anual", fontsize=16)
ax.set_xlabel("Ano")
ax.set_ylabel("Taxa (%)")
ax.legend()
ax.grid(True)

# === Exibir no Streamlit ===
st.pyplot(fig)

# === Exibir tabela com os dados utilizados ===
st.subheader("Dados utilizados no gráfico")
df_display = pd.DataFrame({
    "Ano": anos,
    "SELIC (%)": selic.round(2),
    "IPCA (%)": ipca.round(2),
    "CDI (%)": cdi.round(2)
})
st.dataframe(df_display)
