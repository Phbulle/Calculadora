import streamlit as st

st.title("Calculadora do LF")
valor1 = st.number_input("Digite o Preço 1:", value=None)
valor2 = st.number_input("Digite o Preço 2:", value=None)

lista = [0.10,0.45 , 0.8, 1]
taxas = st.selectbox("Escolha uma taxa:",lista,index=None,placeholder="Escolha uma taxa")

taxa_adicional = st.number_input("Digite a Taxa Adicional:",value=0, placeholder="Digite a Taxa Adicional")

volume = st.number_input("Digite o Volume:" ,value=None)



def lucro(valor1,valor2,taxa,volume):
    if taxa is None:
        st.error("Taxa não pode ser vazia")

    taxa = taxa/100
    valor2 = valor2 - taxa*valor2
    valor_final = (valor2*volume) - (valor1*volume) - taxa_adicional

    st.markdown(f"<h2 style='text-align: center; color: green; font-size: 48px;'>Preço 2: R$ {valor2*volume}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: green; font-size: 48px;'>Preço 1: R$ {valor1*volume}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: #FFFFFF; font-size: 48px;'>Lucro Final: R$ {valor_final}</h2>", unsafe_allow_html=True)


if st.button("Lucro", type="primary"):
    lucro(valor1,valor2,taxas,volume)



