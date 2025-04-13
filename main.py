import os
from etl.coletor_bcb import coletar_dados_selic
from etl.limpeza_selic import limpar_dados_selic
import etl.analise_selic

# Garante que o diretório de dados existe
os.makedirs("etl/dados", exist_ok=True)

# Caminhos dos arquivos
caminho_raw = "etl/dados/selic_raw.csv"
caminho_limpo = "etl/dados/selic_limpo.csv"

# Executa pipeline completo
print("\n[1] Coletando dados da API do Banco Central...")
coletar_dados_selic(caminho_raw)

print("\n[2] Limpando dados coletados...")
limpar_dados_selic(caminho_raw, caminho_limpo)

print("\n[3] Calculando média anual da SELIC...")
media_anual = calcular_media_anual_selic(caminho_limpo)

print("\nMédia anual da SELIC por ano:")
for ano, media in media_anual.items():
    print(f"{ano}: {media:.2f}%")