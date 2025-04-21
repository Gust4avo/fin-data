import requests
import pandas as pd
from datetime import datetime
import os
from utils import garantir_diretorio
from config import SELIC_API_URL

def coletar_dados_selic(caminho_arquivo):
    """
    Coleta dados da SELIC da API do Banco Central e salva em CSV.
    
    Args:
        caminho_arquivo (str): Caminho onde o arquivo CSV será salvo
    """
    garantir_diretorio(caminho_arquivo)

    try:
        response = requests.get(SELIC_API_URL)

        if response.status_code == 200:
            dados = response.json()
            df = pd.DataFrame(dados)
            df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
            df['valor'] = df['valor'].astype(float)

            df.to_csv(caminho_arquivo, index=False)
            print(f"✅ Dados da SELIC salvos com sucesso em '{caminho_arquivo}'.")
        else:
            print(f"❌ Erro ao acessar a API da SELIC: Status {response.status_code}")
    
    except Exception as erro:
        print(f"❌ Ocorreu um erro ao coletar SELIC: {erro}")

if __name__ == "__main__":
    from config import SELIC_RAW
    coletar_dados_selic(SELIC_RAW)