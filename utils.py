import os
import pandas as pd

def garantir_diretorio(caminho_arquivo):
    """Garante que o diretório do arquivo existe"""
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

def ler_dados_financeiros(caminho_arquivo):
    """
    Lê dados financeiros e converte tipos padrão
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo CSV
        
    Returns:
        pandas.DataFrame: DataFrame com dados financeiros
    """
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
        
    df = pd.read_csv(caminho_arquivo)
    df['data'] = pd.to_datetime(df['data'])
    df['valor'] = df['valor'].astype(float)
    df['ano'] = df['data'].dt.year
    return df