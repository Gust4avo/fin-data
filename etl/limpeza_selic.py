import pandas as pd
import os

def limpar_dados_selic(CAMINHO_ARQUIVO):
    df = pd.read_csv(CAMINHO_ARQUIVO)

    df['data'] = pd.to_datetime(df['data'])
    df['valor'] = df['valor'].astype(str).str.replace(',', '.').astype(float)

    if not os.path.exists("dados"):
        os.makedirs("dados")

    df.to_csv(CAMINHO_ARQUIVO, index=False)
    print(" Dados limpos e formatados.")
