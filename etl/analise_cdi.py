import pandas as pd
import os
from utils import garantir_diretorio, ler_dados_financeiros
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calcular_media_anual_cdi(caminho_csv):
    """
    Lê o CSV com dados do CDI diário e calcula a média anual.
    
    Args:
        caminho_csv (str): Caminho para o arquivo CSV com os dados do CDI
        
    Returns:
        pandas.DataFrame: DataFrame com médias anuais do CDI ou None em caso de erro
    """
    if not os.path.exists(caminho_csv):
        logger.error(f"❌ Arquivo não encontrado: {caminho_csv}")
        return None

    try:
        logger.info(f"Lendo arquivo CDI: {caminho_csv}")
        df = ler_dados_financeiros(caminho_csv)
        
        if df.empty:
            logger.error("DataFrame está vazio após leitura")
            return None
            
        # Garantir que temos as colunas necessárias
        if 'ano' not in df.columns or 'valor' not in df.columns:
            logger.error(f"Colunas necessárias não encontradas. Colunas disponíveis: {df.columns.tolist()}")
            return None
            
        media_anual = df.groupby("ano")["valor"].mean().reset_index()
        media_anual.rename(columns={"valor": "media_cdi"}, inplace=True)

        logger.info("📊 Média anual do CDI calculada com sucesso")
        logger.info(f"Forma do DataFrame: {media_anual.shape}")
        
        return media_anual

    except Exception as erro:
        logger.error(f"❌ Erro ao calcular média anual do CDI: {erro}", exc_info=True)
        return None

if __name__ == "__main__":
    from config import CDI_FILE, CDI_ANNUAL_CSV
    
    try:
        garantir_diretorio(CDI_ANNUAL_CSV)
        media_anual = calcular_media_anual_cdi(CDI_FILE)
        
        if media_anual is not None:
            media_anual.to_csv(CDI_ANNUAL_CSV, index=False)
            print(f"✅ CSV com média anual do CDI salvo com sucesso em: {CDI_ANNUAL_CSV}")
        else:
            print("❌ Não foi possível calcular a média anual do CDI")
    
    except Exception as e:
        print(f"❌ Erro ao processar arquivo CDI: {e}")