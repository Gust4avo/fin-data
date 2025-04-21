import os
from etl.coletor_bcb import coletar_dados_selic
from etl.coletor_cdi import coletar_dados_cdi
from etl.limpeza_selic import limpar_dados_selic
from etl.analise_selic import calcular_media_anual_selic, salvar_grafico_media_anual
from etl.analise_cdi import calcular_media_anual_cdi
from config import DATA_DIR, SELIC_RAW, SELIC_CLEAN, CDI_FILE, SELIC_GRAPH, SELIC_ANNUAL_CSV, CDI_ANNUAL_CSV

def main():
    # Garante que o diretório de dados existe
    os.makedirs(DATA_DIR, exist_ok=True)

    print("\n[1] Coletando dados da SELIC...")
    coletar_dados_selic(SELIC_RAW)

    print("\n[2] Coletando dados do CDI...")
    coletar_dados_cdi(CDI_FILE)

    print("\n[3] Limpando dados da SELIC...")
    limpar_dados_selic(SELIC_RAW, SELIC_CLEAN)

    print("\n[4] Calculando média anual da SELIC...")
    media_anual_selic = calcular_media_anual_selic(SELIC_CLEAN)
    media_anual_selic.to_frame(name="media_selic").reset_index().to_csv(SELIC_ANNUAL_CSV, index=False)
    salvar_grafico_media_anual(media_anual_selic, SELIC_GRAPH)

    print("\n[5] Calculando média anual do CDI...")
    media_anual_cdi = calcular_media_anual_cdi(CDI_FILE)
    if media_anual_cdi is not None:
        media_anual_cdi.to_csv(CDI_ANNUAL_CSV, index=False)

    print("\nMédia anual da SELIC por ano:")
    for ano, media in media_anual_selic.items():
        print(f"{ano}: {media:.2f}%")

if __name__ == "__main__":
    main()