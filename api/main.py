import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from etl.analise_selic import calcular_media_anual_selic


CAMINHO_DADOS = "etl/dados/Selic_diaria.csv"

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem" : "API do projeto fin-data está no ar!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

df=pd.read_csv("etl/dados/Selic_diaria.csv")
df["data"] = pd.to_datetime(df["data"])
df["valor"] = df["valor"].astype(str).str.replace(",", ".").astype(float)
df["ano"]= df["data"].dt.year

@app.get("/selic/atual")
def selic_atual():
    dado_mais_recente = df.sort_values("data", ascending=False).iloc[0]
    return{
        "data": dado_mais_recente["data"].strftime("%Y-%m-%d"),
        "valor": dado_mais_recente["valor"]
    }

@app.get("/selic/media-anual")
def selic_media_anual():
    caminho = "etl/dados/Selic_diaria.csv"
    media_ano = calcular_media_anual_selic(caminho)
    return media_ano.round(2).to_dict()