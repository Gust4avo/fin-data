import pandas as pd
import matplotlib.pyplot as plt
import os

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
    df['ano'] = df['data'].dt.year
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

def salvar_grafico_media_anual(media_ano, caminho_imagem):
    """
    Gera e salva um gráfico da média anual da SELIC.
    Args:
        media_ano (pandas.Series): Série com médias anuais
        caminho_imagem (str): Caminho para salvar o arquivo de imagem
    """
    # Criar o diretório para o gráfico se não existir
    os.makedirs(os.path.dirname(caminho_imagem), exist_ok=True)
    
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
    CAMINHO_ARQUIVO = "etl/dados/selic_limpo.csv"
    CAMINHO_GRAFICO = "etl/dados/grafico_media_selic.png"
    CAMINHO_CSV_RESULTADO = "etl/dados/selic_media_anual.csv"
    
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            print(f"ERRO: O arquivo {CAMINHO_ARQUIVO} não foi encontrado!")
            print("Verifique se você executou os scripts na ordem correta:")
            print("1. python etl/coletor_bcb.py")
            print("2. python etl/limpeza_selic.py")
            exit(1)
            
        df = pd.read_csv(CAMINHO_ARQUIVO)
        df['data'] = pd.to_datetime(df['data'])
        df['valor'] = df['valor'].astype(float)
        df['ano'] = df['data'].dt.year
        
        media_ano = calcular_media_anual_selic(CAMINHO_ARQUIVO)
        
        exibir_estatisticas(df)
        print("\n Média anual da SELIC:")
        print(media_ano)
        
        plotar_media_anual(media_ano)
        
        salvar_grafico_media_anual(media_ano, CAMINHO_GRAFICO)
        
        os.makedirs(os.path.dirname(CAMINHO_CSV_RESULTADO), exist_ok=True)
        
        media_ano.to_frame(name="media_selic").reset_index().to_csv(CAMINHO_CSV_RESULTADO, index=False)
        print(f"\n CSV com média anual da SELIC salvo com sucesso em: {CAMINHO_CSV_RESULTADO}")
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        print("Verifique se todos os arquivos necessários existem e os caminhos estão corretos")