import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from api.routers.selic import router as selic_router
from api.routers.cdi import router as cdi_router

app = FastAPI(
    title="API Dados Financeiros",
    description="API para acesso a dados da SELIC e CDI",
    version="1.0.0"
)

# Incluindo os roteadores
app.include_router(selic_router, prefix="/selic", tags=["SELIC"])
app.include_router(cdi_router, prefix="/cdi", tags=["CDI"])

# Liberando acesso para qualquer origem (importante pro Streamlit puxar da API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["Root"])
def root():
    """Rota raiz da API."""
    return {"mensagem": "API do projeto fin-data está no ar!"}

@app.get("/status", tags=["Status"])
def status():
    """Verificar o status da API e disponibilidade de dados."""
    try:
        from config import SELIC_CLEAN, CDI_FILE
        import os
        
        selic_ok = os.path.exists(SELIC_CLEAN)
        cdi_ok = os.path.exists(CDI_FILE)
        
        return {
            "status": "online",
            "dados_selic": "disponíveis" if selic_ok else "indisponíveis",
            "dados_cdi": "disponíveis" if cdi_ok else "indisponíveis"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao verificar status: {str(e)}")