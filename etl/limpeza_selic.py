import pandas as pd
import os
from utils import garantir_diretorio

def limpar_dados_selic(caminho_entrada, caminho_saida):
    """
    Limpa os dados brutos da SELIC.
    
    Args:
        caminho_entrada (str): Caminho do arquivo CSV bruto
        caminho_saida (str): Caminho onde o arquivo CSV limpo será salvo
    """
    try:
        if not os.path.exists(caminho_entrada):
            print(f"❌ Arquivo de entrada não encontrado: {caminho_entrada}")
            return
            
        df = pd.read_csv(caminho_entrada)

        df['data'] = pd.to_datetime(df['data'])
        
        # Tratamento para valores problemáticos
        df['valor'] = df['valor'].astype(str).str.replace(',', '.')
        df['valor'] = pd.to_numeric(df['valor'], errors='coerce')  # 'coerce' converterá valores inválidos para NaN
        df = df.dropna()  # Remove linhas com valores NaN

        garantir_diretorio(caminho_saida)

        df.to_csv(caminho_saida, index=False)
        print(f"✅ Dados limpos e salvos em: {caminho_saida}")
        
    except Exception as erro:
        print(f"❌ Erro ao limpar dados da SELIC: {erro}")

if __name__ == "__main__":
    from config import SELIC_RAW, SELIC_CLEAN
    limpar_dados_selic(SELIC_RAW, SELIC_CLEAN)