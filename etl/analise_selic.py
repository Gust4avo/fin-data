import pandas as pd
import matplotlib.pyplot as plt

def calcular_media_anual_selic(CAMINHO_ARQUIVO):
    """
    Calcula a média anual da taxa SELIC a partir de um arquivo CSV.
    
    Args:
        CAMINHO_ARQUIVO (str): Caminho para o arquivo CSV com os dados da SELIC
        
    Returns:
        pandas.Series: Série com as médias anuais da SELIC
    """
    df = pd.read_csv(CAMINHO_ARQUIVO)
    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year  # Extrai o ano da data
    media_ano = df.groupby('ano')['valor'].mean()
    return media_ano

def exibir_estatisticas(df):
    """
    Exibe estatísticas descritivas do DataFrame da SELIC.
    
    Args:
        df (pandas.DataFrame): DataFrame com os dados da SELIC
    """
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
    """
    Plota um gráfico da média anual da SELIC.
    
    Args:
        media_ano (pandas.Series): Série com as médias anuais da SELIC
    """
    plt.figure(figsize=(10, 5))
    plt.plot(media_ano.index, media_ano.values, marker='o', linestyle='-', color='green')
    plt.title('Média anual da SELIC')
    plt.xlabel('Ano')
    plt.ylabel('Taxa média (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    CAMINHO_ARQUIVO = "etl/dados/Selic_diaria.csv"
    df = pd.read_csv(CAMINHO_ARQUIVO)
    df['data'] = pd.to_datetime(df['data'])
    df['valor'] = df['valor'].astype(float)
    df['ano'] = df['data'].dt.year

    media_ano = calcular_media_anual_selic(CAMINHO_ARQUIVO)

    exibir_estatisticas(df)
    print("\n Média anual da SELIC:")
    print(media_ano)

    plotar_media_anual(media_ano)