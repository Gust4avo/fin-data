
import requests
import pandas as pd
from datetime import datetime

def coletar_dados():
    data_inicial = "01/01/2020"
    data_final = datetime.today().strftime("%d/%m/%Y")

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        df = pd.DataFrame(dados)
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        df['valor'] = df['valor'].astype(float)

        df.to_csv("dados/Selic_diaria.csv", index=False)
        print("✅ Dados salvos com sucesso em 'dados/Selic_diaria.csv'.")
    else:
        print(f"❌ Erro ao acessar a API: {response.status_code}")
