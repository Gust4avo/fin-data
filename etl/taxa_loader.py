import pandas as pd
import os
from datetime import datetime, timedelta
import requests

CAMINHO_SELIC = "etl/dados/selic_limpo.csv" 
URL_API_SELIC = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=csv"

def carregar_taxas_selic():
    # Verifica se o arquivo existe
    if not os.path.exists(CAMINHO_SELIC):
        print("Arquivo CSV não encontrado. Baixando da API...")
        return atualizar_taxas_selic()

    # Carrega o CSV
    df = pd.read_csv(CAMINHO_SELIC, sep=';', decimal=',')
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)

    # Verifica a data do último registro
    data_mais_recente = df['data'].max()
    hoje = datetime.today()

    # Se os dados forem antigos (>30 dias), atualiza
    if hoje - data_mais_recente > timedelta(days=30):
        print("Dados antigos. Atualizando...")
        return atualizar_taxas_selic()
    
    # Dados estão atualizados
    print("Dados do CSV carregados!")
    return df

def atualizar_taxas_selic():
    try:
        print("Baixando dados da API do Banco Central...")
        response = requests.get(URL_API_SELIC)
        response.raise_for_status()

        # Salva o conteúdo em CSV
        with open(CAMINHO_SELIC, "wb") as f:
            f.write(response.content)

        # Carrega o CSV novo
        df = pd.read_csv(CAMINHO_SELIC, sep=';', decimal=',')
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        print("Atualização concluída com sucesso!")
        return df

    except Exception as e:
        print(f"Erro ao baixar da API: {e}")
        return None
