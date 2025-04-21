import os
from datetime import datetime

# Diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "etl", "dados")

# Arquivos
SELIC_RAW = os.path.join(DATA_DIR, "selic_raw.csv")
SELIC_CLEAN = os.path.join(DATA_DIR, "selic_limpo.csv")
CDI_FILE = os.path.join(DATA_DIR, "cdi.csv")
SELIC_GRAPH = os.path.join(DATA_DIR, "grafico_media_selic.png")
SELIC_ANNUAL_CSV = os.path.join(DATA_DIR, "selic_media_anual.csv")
CDI_ANNUAL_CSV = os.path.join(DATA_DIR, "cdi_media_anual.csv")

# Parâmetros de API
API_DATE_FORMAT = "%d/%m/%Y"
API_START_DATE = "01/01/2020"
API_END_DATE = datetime.today().strftime(API_DATE_FORMAT)

# URLs de API
SELIC_API_URL = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial={API_START_DATE}&dataFinal={API_END_DATE}"
CDI_API_URL = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json&dataInicial={API_START_DATE}&dataFinal={API_END_DATE}"