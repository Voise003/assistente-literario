import streamlit as st 

st.title("Meu Assistente Literário")

nome = st.text_input(
    label="Digite seu nome: ",
    value="",
    placeholder="João"
    )


if nome:
     st.write("Olá,", nome)

else : 
      st.write("Digite seu nome acima") 