import requests
import pandas as pd
import os
from datetime import datetime


def coletar_dados_cdi(caminho_saida):
    """
    Coleta os dados do CDI diário da API do Banco Central e salva em CSV.
    """
    try:
        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

        data_inicial = "01/01/2020"
        data_final = datetime.today().strftime("%d/%m/%Y")
        url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"

        resposta = requests.get(url)
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


# Adicione no final do arquivo
if __name__ == "__main__":
    caminho_saida = "etl/dados/cdi.csv"
    coletar_dados_cdi(caminho_saida)