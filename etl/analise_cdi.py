import pandas as pd
import os
from utils import garantir_diretorio, ler_dados_financeiros

def calcular_media_anual_cdi(caminho_csv):
    """
    Lê o CSV com dados do CDI diário e calcula a média anual.
    
    Args:
        caminho_csv (str): Caminho para o arquivo CSV com os dados do CDI
        
    Returns:
        pandas.DataFrame: DataFrame com médias anuais do CDI ou None em caso de erro
    """
    if not os.path.exists(caminho_csv):
        print(f"❌ Arquivo não encontrado: {caminho_csv}")
        return None

    try:
        df = ler_dados_financeiros(caminho_csv)
        media_anual = df.groupby("ano")["valor"].mean().reset_index()
        media_anual.rename(columns={"valor": "media_cdi"}, inplace=True)

        print("📊 Média anual do CDI:")
        print(media_anual)
        
        return media_anual

    except Exception as erro:
        print(f"❌ Erro ao calcular média anual do CDI: {erro}")
        return None

if __name__ == "__main__":
    from config import CDI_FILE, CDI_ANNUAL_CSV
    
    try:
        garantir_diretorio(CDI_ANNUAL_CSV)
        media_anual = calcular_media_anual_cdi(CDI_FILE)
        
        if media_anual is not None:
            media_anual.to_csv(CDI_ANNUAL_CSV, index=False)
            print(f"✅ CSV com média anual do CDI salvo com sucesso em: {CDI_ANNUAL_CSV}")
    
    except Exception as e:
        print(f"❌ Erro ao processar arquivo CDI: {e}")