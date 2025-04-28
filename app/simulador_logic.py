from datetime import datetime, timedelta
import requests
import logging

# Configurar logging básico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calcular_simulacao(saldo_inicial, aporte_mensal, meta, tipo):
    """
    Calcula simulação de investimento baseado em diferentes tipos de rendimento.
    
    Args:
        saldo_inicial (float): Valor inicial a ser investido
        aporte_mensal (float): Valor a ser adicionado mensalmente
        meta (float): Valor alvo a ser atingido
        tipo (str): Tipo de investimento (Conservador, Moderado, Agressivo, SELIC ou CDI)
        
    Returns:
        tuple: (meses, historico, total_aportado, rendimento_estimado, data_final)
    """
    # Definir taxa de juros
    taxas_fixas = {
        "Conservador (0.5% a.m.)": 0.005,
        "Moderado (0.8% a.m.)": 0.008,
        "Agressivo (1.2% a.m.)": 0.012
    }

    if tipo in taxas_fixas:
        taxa_mensal = taxas_fixas[tipo]
        logger.info(f"Usando taxa fixa: {taxa_mensal:.4f} ao mês")
    else:
        # Buscar taxa SELIC ou CDI
        try:
            if tipo == "SELIC":
                url = "http://localhost:8000/selic/media-anual"
            else:  # CDI
                url = "http://localhost:8000/cdi/media-anual"
                
            logger.info(f"Buscando dados de {url}")
            response = requests.get(url)
            
            # Registrar detalhes da resposta para diagnóstico
            logger.info(f"Status code: {response.status_code}")
            logger.info(f"Resposta: {response.text[:200]}...")  # Primeiros 200 caracteres
            
            response.raise_for_status()
            dados = response.json()
            
            logger.info(f"Dados recebidos: {dados}")

            if tipo == "SELIC":
                # A API SELIC retorna um dicionário de ano -> valor
                try:
                    # Se é um dicionário de anos
                    anos = sorted([int(ano) for ano in dados.keys()])
                    media_anual = float(dados[str(anos[-1])])
                except (ValueError, KeyError, TypeError):
                    # Se não for um dicionário de anos, tenta formato alternativo
                    if isinstance(dados, dict) and "media_anual" in dados:
                        media_anual = float(dados["media_anual"])
                    else:
                        # Valor padrão razoável se não conseguir determinar
                        logger.warning("Não foi possível determinar a taxa SELIC. Usando 10%.")
                        media_anual = 10.0
            else:  # CDI
                # A API CDI retorna {"media_anual": valor}
                if isinstance(dados, dict) and "media_anual" in dados:
                    media_anual = float(dados["media_anual"])
                else:
                    # Outro formato ou valor padrão
                    logger.warning("Não foi possível determinar a taxa CDI. Usando 9.5%.")
                    media_anual = 9.5
                    
            logger.info(f"Taxa anual obtida: {media_anual:.4f}%")
            
            # Converter taxa anual para mensal
            # A taxa vem em percentual (ex: 13.75), então dividimos por 100
            taxa_mensal = (1 + media_anual/100) ** (1/12) - 1
            logger.info(f"Taxa mensal calculada: {taxa_mensal:.6f}")
            
        except Exception as e:
            # Em caso de erro, usar uma taxa padrão e alertar
            logger.error(f"Erro ao obter taxa: {str(e)}")
            if tipo == "SELIC":
                taxa_mensal = 0.009  # ~11% ao ano
                logger.warning("Usando taxa SELIC padrão de 0.9% ao mês")
            else:  # CDI
                taxa_mensal = 0.008  # ~10% ao ano
                logger.warning("Usando taxa CDI padrão de 0.8% ao mês")

    # Cálculo da simulação
    saldo = saldo_inicial
    meses = 0
    historico = []

    # Loop de simulação
    while saldo < meta and meses < 600:  # Máximo de 50 anos para evitar loop infinito
        saldo += saldo * taxa_mensal
        saldo += aporte_mensal
        historico.append(saldo)
        meses += 1

    total_aportado = saldo_inicial + (aporte_mensal * meses)
    rendimento_estimado = saldo - total_aportado
    data_final = datetime.today() + timedelta(days=30*meses)

    return meses, historico, total_aportado, rendimento_estimado, data_final