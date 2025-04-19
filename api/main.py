import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from etl.analise_selic import calcular_media_anual_selic
from api.routers.selic import router as selic_router

CAMINHO_DADOS = "etl/dados/selic_limpo.csv"


app = FastAPI()

app.include_router(selic_router)

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


