from fastapi import APIRouter, HTTPException
from etl.analise_selic import calcular_media_anual_selic
from config import SELIC_CLEAN

router = APIRouter(prefix="/selic", tags=["SELIC"])

@router.get("/media-anual")
def media_anual_selic():
    """
    Retorna a média anual da SELIC.
    Exemplo de retorno: {"media_anual": 13.75}
    """
    try:
        media = calcular_media_anual_selic(SELIC_CLEAN)
        if media is None:
            raise HTTPException(status_code=404, detail="Dados SELIC não disponíveis")
        # Retorna um dicionário simples com a média arredondada
        return {"media_anual": round(media, 4)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao calcular média SELIC: {e}")

@router.get("/atual")
def selic_atual():
    """Retorna o valor mais recente da SELIC."""
    try:
        # Se você quiser manter este endpoint, tudo bem
        from utils import ler_dados_financeiros
        df = ler_dados_financeiros(SELIC_CLEAN)
        ultima = df.iloc[-1]
        return {
            "data": ultima["data"].strftime("%Y-%m-%d"),
            "valor": round(ultima["valor"], 4)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter valor atual: {e}")

@router.get("/tabela-completa")
def tabela_completa():
    """Retorna todos os registros da SELIC."""
    try:
        from utils import ler_dados_financeiros
        df = ler_dados_financeiros(SELIC_CLEAN)
        df['data'] = df['data'].dt.strftime("%Y-%m-%d")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter tabela completa: {e}")

@router.get("/por-ano/{ano}")
def selic_por_ano(ano: int):
    """Retorna os registros da SELIC de um ano específico."""
    try:
        from utils import ler_dados_financeiros
        df = ler_dados_financeiros(SELIC_CLEAN)
        filtro = df[df['ano'] == ano]
        if filtro.empty:
            raise HTTPException(status_code=404, detail=f"Não há dados para o ano {ano}")
        filtro['data'] = filtro['data'].dt.strftime("%Y-%m-%d")
        return filtro.to_dict(orient="records")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter dados por ano: {e}")
