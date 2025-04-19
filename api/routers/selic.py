from fastapi import APIRouter
from fastapi.responses import JSONResponse
from etl.analise_selic import calcular_media_anual_selic


CAMINHO_DADOS = "etl/dados/selic_limpo.csv"

router = APIRouter()


@router.get("/selic/media-anual-json")
def media_anual_json():
    media = calcular_media_anual_selic(CAMINHO_DADOS)
    return JSONResponse(content=media.round(2).to_dict())