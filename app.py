import streamlit as st


def gerar_analise(livro):
    return f"""
## 📖 Análise de {livro}

### Contexto histórico

Esta seção apresentará o contexto histórico e cultural relacionado à obra.

### Temas principais

- Conflitos humanos
- Relações sociais
- Transformação dos personagens
- Questões morais e existenciais

### Personagens

Aqui serão apresentados os principais personagens e seus papéis na narrativa.

### Simbolismos

Esta seção mostrará possíveis símbolos presentes na obra e seus significados.

### Observação

Esta é uma análise simulada. Futuramente, ela será substituída por uma análise gerada por inteligência artificial.
"""


st.set_page_config(
    page_title="Assistente Literário",
    page_icon="📚"
)

st.title("Meu Assistente Literário")

st.write(
    "Digite o nome de uma obra para receber uma análise literária estruturada."
)

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

analisar = st.button("Analisar")

if analisar:
    if not livro.strip():
        st.warning("Digite o nome do livro.")
    else:
        with st.spinner("Preparando a análise..."):
            resultado = gerar_analise(livro)

        st.success("Análise concluída.")
        st.markdown(resultado)