# fin-data/simulador_logic.py

from datetime import datetime, timedelta

def calcular_simulacao(saldo_inicial, aporte_mensal, meta, tipo, taxas_fixas, dados_taxas):
    saldo = saldo_inicial
    historico = []
    total_aportado = 0.0
    meses = 0
    hoje = datetime.today()

    if tipo in taxas_fixas:
        # Taxa fixa
        taxa = taxas_fixas[tipo]
        while saldo < meta:
            saldo += saldo * taxa + aporte_mensal
            total_aportado += aporte_mensal
            historico.append(saldo)
            meses += 1
    else:
        # Taxa variável (SELIC, CDI)
        taxas = dados_taxas[tipo]
        i = 0
        while saldo < meta:
            taxa = taxas[i % len(taxas)]
            saldo += saldo * taxa + aporte_mensal
            total_aportado += aporte_mensal
            historico.append(saldo)
            meses += 1
            i += 1

    rendimento_estimado = saldo - saldo_inicial - total_aportado
    data_final = hoje + timedelta(days=30 * meses)

    return meses, historico, total_aportado, rendimento_estimado, data_final
