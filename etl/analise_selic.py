import pandas as pd
import matplotlib.pyplot as plt

def calcular_media_anual(CAMINHO_ARQUIVO):
    df = pd.read_csv(CAMINHO_ARQUIVO)
    df['data'] = pd.to_datetime(df['data'])
    media_ano = df.groupby('ano')['valor'].mean()
    return media_ano

def exibir_estatisticas(df):
    print("\n📋 Informações do DataFrame:")
    print(df.info())

    print("\n Estatísticas descritivas:")
    print(df.describe())

    dias_zero = df[df['valor'] == 0]
    print(f"\n Dias com SELIC igual a 0: {len(dias_zero)}")

    print(f"\n Mínima: {df['valor'].min()}%")
    print(f" Máxima: {df['valor'].max()}%")
    print(f"Média: {df['valor'].mean():.2f}%")
    print(f" Moda: {df['valor'].mode()[0]}%")

def plotar_media_anual(media_ano):
    plt.figure(figsize=(10, 5))
    plt.plot(media_ano.index, media_ano.values * 100, marker='o', linestyle='-', color='green')
    plt.title('Média anual da SELIC')
    plt.xlabel('Ano')
    plt.ylabel('Taxa média (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("etl/dados/Selic_diaria.csv")
    df['data'] = pd.to_datetime(df['data'])
    df['valor'] = df['valor'].astype(float)

    media_ano = calcular_media_anual(df)

    exibir_estatisticas(df)
    print("\n Média anual da SELIC:")
    print(media_ano)

    plotar_media_anual(media_ano)
