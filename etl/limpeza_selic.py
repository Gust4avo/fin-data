import pandas as pd
import os

def limpar_dados_selic(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada)

    df['data'] = pd.to_datetime(df['data'])
    df['valor'] = df['valor'].astype(str).str.replace(',', '.').astype(float)

    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

    df.to_csv(caminho_saida, index=False)
    print(" Dados limpos e salvos em:", caminho_saida)
