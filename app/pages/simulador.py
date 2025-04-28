import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from babel.dates import format_date
import sys
import os

# Adiciona o diretório raiz ao path de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Importa a função do simulador
from simulador_logic import calcular_simulacao

# Título e descrição
st.title("Simulador de Investimento Real")
st.markdown("Preencha os dados abaixo para estimar quando você atingirá sua meta de investimento.")

# Formulário de entrada
col1, col2 = st.columns(2)
with col1:
    saldo_inicial = st.number_input("Saldo Inicial (R$)", min_value=0.0, value=1000.0, step=100.0)
    aporte_mensal = st.number_input("Aporte Mensal (R$)", min_value=0.0, value=500.0, step=50.0)
with col2:
    meta = st.number_input("Meta (R$)", min_value=100.0, value=20000.0, step=500.0)
    tipo = st.selectbox(
        "Tipo de Investimento",
        ["Conservador (0.5% a.m.)", "Moderado (0.8% a.m.)", "Agressivo (1.2% a.m.)", "SELIC", "CDI"]
    )

# Status para mostrar mensagens de carregamento
status = st.empty()

# Botão calcular
if st.button("Calcular"):
    with st.spinner("Buscando taxas atualizadas e calculando..."):
        # A função agora busca os dados da API automaticamente quando necessário
        meses, historico, total_aportado, rendimento_estimado, data_final = calcular_simulacao(
            saldo_inicial, aporte_mensal, meta, tipo
        )

    # Resultados
    anos, meses_restantes = divmod(meses, 12)
    st.success(f"Você atingirá sua meta em {meses} meses ({anos} anos e {meses_restantes} meses)")
    st.info(f"Total aportado: R$ {total_aportado:,.2f}")
    st.info(f"Rendimento estimado: R$ {rendimento_estimado:,.2f}")
    
    data_formatada = format_date(data_final, "MMMM/yyyy", locale='pt_BR').capitalize()
    st.info(f"Data prevista: {data_formatada}")

    # Gráfico de evolução
    df = pd.DataFrame({"Saldo acumulado": historico})
    df.index = [f"{i+1}º mês" for i in range(len(df))]
    fig, ax = plt.subplots()
    df.plot(ax=ax, legend=False, color="limegreen")
    ax.set_title("Evolução do saldo acumulado")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Saldo (R$)")
    st.pyplot(fig)

# Link para home
st.markdown("[Voltar à Home](../1_home.py)")