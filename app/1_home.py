import streamlit as st

# Espaçar um pouco do topo
st.write("")
st.write("")


caminho_icon = "figuras/icon.png"
# imagem do topo
st.image(caminho_icon, width=100)  # ícone CDN

# Título centralizado
st.markdown("<h1 style='text-align: center; color: white;'>Bem-vindo ao FinData</h1>", unsafe_allow_html=True)

st.write("")
st.write("")

# Card bonito com as informações
with st.container():
    st.markdown(
        """
        <div style="background-color: #262730; padding: 20px; border-radius: 10px;">
            <h3 style="color: #4CAF50;">📊 O que você pode acompanhar aqui:</h3>
            <ul style="color: white; font-size: 18px;">
                <li>✅ <b>SELIC</b>: taxa básica de juros do país</li>
                <li>✅ <b>IPCA</b>: índice oficial de inflação</li>
                <li>✅ <b>CDI</b>: taxa média do mercado interbancário</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# Um espaço final
st.write("")
st.write("")
st.divider()
st.caption("FinData © 2025 - Projeto em desenvolvimento 🚀")
