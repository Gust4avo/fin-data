import pandas as pd

def calcular_media_anual_ipca(caminho_csv):
    df = pd.read_csv(caminho_csv)
    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year

    media_anual = df.groupby('ano')['valor'].mean().reset_index()
    return media_anual


if __name__ == "__main__":
    caminho_ipca = "etl/dados/ipca.csv"
    caminho_saida = "etl/dados/ipca_anual.csv"

    media_ipca = calcular_media_anual_ipca(caminho_ipca)
    media_ipca.to_csv(caminho_saida, index=False)

    print("✅ Média anual do IPCA salva em:", caminho_saida)