import requests
import pandas as pd
from datetime import datetime
import os  # Importar a biblioteca os para manipulação de diretórios

def coletar_dados_selic(CAMINHO_ARQUIVO):
    pasta = os.path.dirname(CAMINHO_ARQUIVO)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    data_inicial = "01/01/2020"
    data_final = datetime.today().strftime("%d/%m/%Y")

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        df = pd.DataFrame(dados)
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        df['valor'] = df['valor'].astype(float)

        df.to_csv(CAMINHO_ARQUIVO, index=False)  # Salvar no caminho recebido
        print(f"Dados salvos com sucesso em '{CAMINHO_ARQUIVO}'.")
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
