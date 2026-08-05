import streamlit as st

from prompts import PROMPTS
from analise import gerar_analise

if "historico" not in st.session_state:
    st.session_state.historico = []

st.set_page_config(
    page_title="Assistente Literário",
    page_icon="📚",
    layout="centered"
)

st.title("Assistente Literário")

st.markdown(
    """
Explore obras literárias por meio de análises estruturadas.

Escolha o tipo de análise, informe o nome da obra e clique em **Analisar**.
"""
)

st.divider() 

livro = st.text_input(
    "Nome do livro",
    placeholder="Ex.: Senhor das Moscas"
)

tipo_analise = st.selectbox(
    "Tipo de análise",
    [
        "Análise completa",
        "Resumo",
        "Personagens",
        "Temas",
        "Simbolismos"
    ]
)

prompt = PROMPTS[tipo_analise]

analisar = st.button(
    "Analisar obra",
    type="primary",
    use_container_width=True
)

if analisar:
    if not livro.strip():
        st.warning("Digite o nome do livro.")
    else:
        with st.spinner("Preparando a análise..."):
            resultado = gerar_analise(livro, prompt)
            st.session_state.historico.append({
            "livro": livro,
            "tipo": tipo_analise,
            "resultado": resultado
})

        st.success("Análise concluída.")
        with st.container(border=True):
            st.markdown(resultado)

    st.download_button(
    label="⬇️ Baixar análise",
    data=resultado,
    file_name=f"analise_{livro}.md",
    mime="text/markdown",
    use_container_width=True
)
    
    st.divider()

st.subheader("📚 Histórico")

if not st.session_state.historico:
    st.info("Nenhuma análise realizada nesta sessão.")
else:
    for item in reversed(st.session_state.historico):
        with st.expander(f"{item['livro']} - {item['tipo']}"):
            st.markdown(item["resultado"])