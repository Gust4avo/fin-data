import pandas as pd

def limpar_dados():
    df = pd.read_csv("dados/Selic_diaria.csv")
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['valor'] = df['valor'].str.replace(',', '.').astype(float)
    df.to_csv("dados/Selic_diaria.csv", index=False)
    print("✅ Dados limpos e formatados.")