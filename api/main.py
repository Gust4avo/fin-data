import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from etl.analise_selic import calcular_media_anual_selic

CAMINHO_DADOS = "etl/dados/selic_limpo.csv"

app = FastAPI()

# Liberando acesso para qualquer origem (importante pro Streamlit puxar da API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"mensagem": "API do projeto fin-data está no ar!"}

@app.get("/selic/media-anual-json")
def media_anual_json():
    media = calcular_media_anual_selic(CAMINHO_DADOS)
    return JSONResponse(content=media.round(2).to_dict())
