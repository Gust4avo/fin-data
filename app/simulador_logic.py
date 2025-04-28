from datetime import datetime, timedelta
import requests

def calcular_simulacao(saldo_inicial, aporte_mensal, meta, tipo):
    # Definir taxa de juros
    taxas_fixas = {
        "Conservador (0.5% a.m.)": 0.005,
        "Moderado (0.8% a.m.)": 0.008,
        "Agressivo (1.2% a.m.)": 0.012
    }

    if tipo in taxas_fixas:
        taxa_mensal = taxas_fixas[tipo]
    else:
        # Buscar taxa SELIC ou CDI
        response = requests.get("http://localhost:8000/cdi/media-anual")
        response.raise_for_status()
        dados = response.json()

        if not dados:
            raise ValueError("Nenhum dado de média anual recebido da API.")

        media_anual = dados[-1]["media"]
        taxa_mensal = (1 + media_anual) ** (1/12) - 1

    saldo = saldo_inicial
    meses = 0
    historico = []

    while saldo < meta:
        saldo += saldo * taxa_mensal
        saldo += aporte_mensal
        historico.append(saldo)
        meses += 1

    total_aportado = saldo_inicial + (aporte_mensal * meses)
    rendimento_estimado = saldo - total_aportado
    data_final = datetime.today() + timedelta(days=30*meses)

    return meses, historico, total_aportado, rendimento_estimado, data_final
