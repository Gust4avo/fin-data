# 📊 fin-data

Projeto de engenharia de dados e visualização interativa com foco em educação financeira acessível.

## 💡 Propósito

O **fin-data** nasceu de uma inquietação real: muitas pessoas não guardam dinheiro por acharem complicado investir ou por não entenderem como a economia influencia suas decisões.

🎯 A proposta é transformar dados econômicos (como a **taxa SELIC**) em **informações visuais e simples**, ajudando pessoas comuns a entenderem melhor seus impactos no dia a dia.

---

## 🚀 O que o projeto já faz

✅ **Coleta dados diretamente da API do Banco Central**  
✅ **Processa os dados com ETL em Python**  
✅ **Calcula a média anual da SELIC automaticamente**  
✅ **Exibe os dados com visualização interativa em Streamlit**  
✅ **Permite filtrar anos, comparar com CDI e IPCA**  
✅ **Oferece download em CSV dos dados tratados**

---

## 👨‍💻 Tecnologias utilizadas

- Python 3.10+
- FastAPI (serviço backend com endpoints de dados)
- Streamlit (dashboard interativo)
- Matplotlib & Pandas (visualização e análise)
- Banco Central do Brasil (API pública)
- Arquitetura ETL (Extração, Transformação, Carga)

---

## 🧹 Estrutura do Projeto

```
fin-data/
🔜 api/                  # Endpoints FastAPI
├── routers/
└── main.py
🔜 app/                  # Interface interativa Streamlit
├── pages/
│   ├── comparativo_selic_ipca_cdi.py
│   ├── dashboard_selic.py
│   └── home.py
└── streamlit_dashboard.py
🔜 etl/                  # Scripts de coleta, limpeza e análise
├── dados/            # CSVs e figuras geradas
├── analise_selic.py
├── analise_ipca.py
├── analise_cdi.py
├── limpeza_selic.py
├── coletor_bcb.py
└── visualiza_selic.py
main.py               # Orquestrador do pipeline
requirements.txt
README.md
```

---

## 🔮 Próximos desafios

- [ ] Criar explicações automáticas com **IA integrada (ChatGPT API)**
- [ ] Adicionar indicadores como **poupança e Tesouro Selic**
- [ ] **Simplificar visualmente os dados** para serem compreendidos até por quem nunca estudou economia
- [ ] Criar um modo "educativo" com **textos acessíveis e exemplos práticos**
- [ ] Publicar o projeto na **AWS (EC2 ou Lambda + S3)**
- [ ] Melhorar responsividade da interface (mobile-friendly)

---

## 📷 Exemplo do Dashboard

![Exemplo de gráfico comparativo](figuras/grafico_media_selic.png)

---

---

