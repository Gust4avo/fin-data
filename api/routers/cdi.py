from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from etl.analise_cdi import calcular_media_anual_cdi
import pandas as pd
from config import CDI_FILE
from utils import ler_dados_financeiros

router = APIRouter()

@router.get("/media-anual")
def media_anual_json():
    """Retorna a média anual do CDI."""
    try:
        media = calcular_media_anual_cdi(CDI_FILE)
        if media is not None:
            return JSONResponse(content=media.to_dict(orient="records"))
        raise HTTPException(status_code=404, detail="Dados do CDI não disponíveis")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao calcular média anual: {str(e)}")

@router.get("/atual")
def cdi_atual():
    """Retorna o valor mais recente do CDI."""
    try:
        df = ler_dados_financeiros(CDI_FILE)
        ultima_linha = df.iloc[-1]
        data = ultima_linha["data"].strftime("%Y-%m-%d")
        valor = ultima_linha["valor"]
        return JSONResponse(content={"data": data, "valor": round(valor, 2)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter valor atual: {str(e)}")

@router.get("/tabela-completa")
def tabela_completa():
    """Retorna a tabela completa de dados do CDI."""
    try:
        df = ler_dados_financeiros(CDI_FILE)
        df['data'] = df['data'].dt.strftime("%Y-%m-%d")
        return JSONResponse(content=df.to_dict(orient="records"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter tabela completa: {str(e)}")

@router.get("/por-ano/{ano}")
def cdi_por_ano(ano: int):
    """Retorna os valores do CDI para um ano específico."""
    try:
        df = ler_dados_financeiros(CDI_FILE)
        filtro = df[df['ano'] == ano]
        
        if filtro.empty:
            raise HTTPException(status_code=404, detail=f"Não foram encontrados dados para o ano {ano}")
            
        filtro['data'] = filtro['data'].dt.strftime("%Y-%m-%d")
        return JSONResponse(content=filtro.to_dict(orient="records"))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter dados por ano: {str(e)}")