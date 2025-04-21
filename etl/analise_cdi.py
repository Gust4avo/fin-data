import pandas as pd
import os

def calcular_media_anual_cdi(caminho_csv):
    """
    Lê o CSV com dados do CDI diário e calcula a média anual.
    """
    if not os.path.exists(caminho_csv):
        print(f"❌ Arquivo não encontrado: {caminho_csv}")
        return

    try:
        df = pd.read_csv(caminho_csv)
        df["data"] = pd.to_datetime(df["data"])
        df["ano"] = df["data"].dt.year

        media_anual = df.groupby("ano")["valor"].mean().reset_index()
        media_anual.rename(columns={"valor": "media_cdi"}, inplace=True)

        print("📊 Média anual do CDI:")
        print(media_anual)

    except Exception as erro:
        print(f"❌ Erro ao calcular média anual do CDI: {erro}")
