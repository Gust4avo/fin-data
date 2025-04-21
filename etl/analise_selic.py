import pandas as pd
import matplotlib.pyplot as plt
import os
from utils import garantir_diretorio, ler_dados_financeiros

def calcular_media_anual_selic(caminho_arquivo):
    """
    Calcula a média anual da taxa SELIC a partir de um arquivo CSV.
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo CSV com os dados da SELIC
    
    Returns:
        pandas.Series: Série com as médias anuais da SELIC
    """
    try:
        df = ler_dados_financeiros(caminho_arquivo)
        media_ano = df.groupby('ano')['valor'].mean()
        return media_ano
    except Exception as e:
        print(f"Erro ao calcular média anual da SELIC: {e}")
        return pd.Series()

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

def salvar_grafico_media_anual(media_ano, caminho_imagem):
    """
    Gera e salva um gráfico da média anual da SELIC.
    
    Args:
        media_ano (pandas.Series): Série com médias anuais
        caminho_imagem (str): Caminho para salvar o arquivo de imagem
    """
    garantir_diretorio(caminho_imagem)
    
    plt.figure(figsize=(10, 5))
    plt.plot(media_ano.index, media_ano.values, marker='o', linestyle='-', color='green')
    plt.title('Média anual da SELIC')
    plt.xlabel('Ano')
    plt.ylabel('Taxa média (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(caminho_imagem)
    print(f"\n Gráfico salvo em: {caminho_imagem}")

def plotar_media_anual(media_ano):
    """
    Plota um gráfico da média anual da SELIC (exibe na tela).
    
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
    from config import SELIC_CLEAN, SELIC_GRAPH, SELIC_ANNUAL_CSV
    
    try:
        df = ler_dados_financeiros(SELIC_CLEAN)
        
        media_ano = calcular_media_anual_selic(SELIC_CLEAN)
        
        exibir_estatisticas(df)
        print("\n Média anual da SELIC:")
        print(media_ano)
        
        plotar_media_anual(media_ano)
        
        salvar_grafico_media_anual(media_ano, SELIC_GRAPH)
        
        garantir_diretorio(SELIC_ANNUAL_CSV)
        media_ano.to_frame(name="media_selic").reset_index().to_csv(SELIC_ANNUAL_CSV, index=False)
        print(f"\n CSV com média anual da SELIC salvo com sucesso em: {SELIC_ANNUAL_CSV}")
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        print("Verifique se todos os arquivos necessários existem e os caminhos estão corretos")