# **fin-data** 📊

## **Sobre o Projeto**  
O **fin-data** é uma iniciativa pessoal criada para ajudar qualquer pessoa, mesmo sem experiência em finanças, a entender como a **taxa SELIC** impacta seus investimentos. Usando dados abertos do Banco Central, **Python** e **Streamlit**, o projeto oferece uma maneira simples e interativa de analisar a SELIC ao longo dos anos e tomar decisões financeiras mais informadas.

---

## **Funcionalidades**  
- **Visualização interativa da média anual da SELIC**
- **Filtros por ano** para análises personalizadas
- **Download dos dados em CSV** para uso pessoal
- **API** para acessar dados atualizados da SELIC
- **Futuro: IA para explicações mais detalhadas**

---

## **Como Usar**  
1. **Clone o repositório**  
   ```bash
   git clone https://github.com/seu-usuario/fin-data.git
   cd fin-data
   pip install -r requirements.txt
   uvicorn api.main:app --reload
   uvicorn api.main:app --reload

## **Exemplos de Uso**
- **Investidores de Renda Fixa**: Acompanhe como a SELIC afeta a rentabilidade de produtos como CDBs e Tesouro Direto.  
- **Planejamento Financeiro**: Use a média anual da SELIC para entender o impacto de mudanças nas taxas de juros sobre seus investimentos.  
- **Análise Econômica**: Analistas podem estudar a SELIC para prever tendências econômicas e o impacto da política monetária.  
- **Educação Financeira**: Ferramenta útil para ensinar conceitos econômicos de forma interativa e acessível.

## **Tecnologias**
- Python  
- FastAPI  
- Streamlit  
- pandas  
- requests

## **Futuras Melhorias**
- Integração com IA para explicações mais detalhadas sobre os dados  
- Adição de dados sobre ações e comparações entre diferentes tipos de investimento  
- Deploy em Nuvem (AWS)
