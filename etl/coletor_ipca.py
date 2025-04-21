import requests
import pandas as pd

def coletor_ipca():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2000&dataFinal=31/12/2025"

    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        df = pd.DataFrame(dados)
        df.columns = ['data', 'valor']
        df.to_csv("etl/dados/ipca.csv", index=False)
        print("✅ IPCA salvo em etl/dados/ipca.csv")
    else:
        print("❌ Erro ao coletar dados do IPCA. Status:", resposta.status_code)

if __name__ == "__main__":
    coletor_ipca()
