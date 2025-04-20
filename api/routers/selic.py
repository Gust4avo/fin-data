from fastapi import APIRouter
from fastapi.responses import JSONResponse
from etl.analise_selic import calcular_media_anual_selic
import pandas as pd

CAMINHO_DADOS = "etl/dados/selic_limpo.csv"

router = APIRouter()


@router.get("/selic/media-anual-json")
def media_anual_json():
    media = calcular_media_anual_selic(CAMINHO_DADOS)
    return JSONResponse(content=media.round(2).to_dict())


@router.get("/selic/atual")
def selic_atual():
    df = pd.read_csv(CAMINHO_DADOS)
    ultima_linha = df.iloc[-1]
    data = ultima_linha["data"]
    valor = ultima_linha["valor"]
    return JSONResponse(content={"data": data, "valor": round(valor, 2)})


@router.get("/selic/tabela-completa")
def tabela_completa():
    df = pd.read_csv(CAMINHO_DADOS)
    return JSONResponse(content=df.to_dict(orient="records"))