from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from etl.analise_cdi import calcular_media_anual_cdi
import pandas as pd
import os
from config import CDI_FILE
from utils import ler_dados_financeiros

router = APIRouter(prefix="/cdi", tags=["CDI"])

@router.get("/media-anual")
def media_anual_json():
    """Retorna a média anual do CDI."""
    try:
        # Primeiro, verificar se o arquivo existe
        if not os.path.exists(CDI_FILE):
            raise HTTPException(status_code=404, detail=f"Arquivo CDI não encontrado: {CDI_FILE}")
            
        media = calcular_media_anual_cdi(CDI_FILE)
        
        if media is None:
            raise HTTPException(status_code=404, detail="Dados do CDI não disponíveis")
            
        # Verificar se a média é um DataFrame com estrutura esperada
        if isinstance(media, pd.DataFrame) and "ano" in media.columns and "media_cdi" in media.columns:
            # Extrair o valor mais recente (última linha)
            if not media.empty:
                ano_recente = media["ano"].max()
                media_recente = media[media["ano"] == ano_recente]["media_cdi"].iloc[0]
                return JSONResponse(content={"media_anual": round(float(media_recente), 4)})
            else:
                raise HTTPException(status_code=404, detail="DataFrame de média do CDI está vazio")
        else:
            # Fallback para outros formatos
            return JSONResponse(content={"media_anual": round(float(media), 4)})
            
    except HTTPException:
        raise
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