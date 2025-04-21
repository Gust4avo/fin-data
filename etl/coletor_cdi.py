import requests
import pandas as pd
import os
from datetime import datetime
from utils import garantir_diretorio
from config import CDI_API_URL

def coletar_dados_cdi(caminho_saida):
    """
    Coleta os dados do CDI diário da API do Banco Central e salva em CSV.
    
    Args:
        caminho_saida (str): Caminho onde o arquivo CSV será salvo
    """
    try:
        garantir_diretorio(caminho_saida)

        resposta = requests.get(CDI_API_URL)
        if resposta.status_code != 200:
            print(f"❌ Erro ao acessar a API do CDI: Status {resposta.status_code}")
            return

        dados = resposta.json()
        df = pd.DataFrame(dados)
        df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
        df["valor"] = df["valor"].astype(float)

        df.to_csv(caminho_saida, index=False)
        print(f"✅ Dados do CDI salvos com sucesso em: {caminho_saida}")

    except Exception as erro:
        print(f"❌ Ocorreu um erro ao coletar CDI: {erro}")

if __name__ == "__main__":
    from config import CDI_FILE
    coletar_dados_cdi(CDI_FILE)