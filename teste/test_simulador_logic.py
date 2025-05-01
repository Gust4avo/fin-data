import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import datetime, timedelta
from app.simulador_logic import calcular_simulacao

class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code
        self.text = str(json_data)
    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise Exception(f"HTTP {self.status_code}")
    def json(self):
        return self._json

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    # Bloqueia chamadas reais de requests.get
    import requests
    monkeypatch.setattr(requests, "get", lambda url: DummyResponse({"media_anual": 12.0}))

def test_sem_aporte_saldo_inicial_only():
    meses, hist, total, rend, dataf = calcular_simulacao(
        saldo_inicial=1000.0,
        aporte_mensal=0.0,
        meta=1100.0,
        tipo="Conservador (0.5% a.m.)"
    )
    # 0.5% ao mês gera ~5 reais de juros por mês; em 2 meses atinge
    assert meses >= 2
    assert hist[0] == pytest.approx(1000 * 1.005)
    # Total aportado é só o inicial
    assert total == pytest.approx(1000.0)
    # Data final está num futuro razoável
    assert dataf.date() >= datetime.today().date()

def test_aporte_zero_taxa_zero():
    meses, hist, total, rend, _ = calcular_simulacao(
        saldo_inicial=0.0,
        aporte_mensal=100.0,
        meta=500.0,
        tipo="CDI"  # via dummy retorna 12% a.a. → ~0.9489% a.m.
    )
    # Mesmo com taxa, garantimos que total_aportado bate a meta
    assert total == pytest.approx(100.0 * meses)
    assert hist[-1] >= 500.0

def test_meta_alcançada_imediata():
    meses, hist, total, rend, _ = calcular_simulacao(
        saldo_inicial=2000.0,
        aporte_mensal=100.0,
        meta=1500.0,
        tipo="Moderado (0.8% a.m.)"
    )
    # Meta já no saldo inicial → meses zero
    assert meses == 0
    assert hist == []
    assert total == pytest.approx(2000.0)

def test_fallback_taxa_padrao_selic(monkeypatch):
    # Simula falha na API
    import requests
    monkeypatch.setattr(requests, "get", lambda url: DummyResponse({}, status_code=500))
    meses, hist, total, rend, _ = calcular_simulacao(
        saldo_inicial=1000.0,
        aporte_mensal=100.0,
        meta=1200.0,
        tipo="SELIC"
    )
    # Usa fallback ~0.9% a.m., então em 2 meses →
    assert meses >= 2
    assert total == pytest.approx(1000.0 + 100.0 * meses)

# Para executar:
# > pytest --maxfail=1 --disable-warnings -q
