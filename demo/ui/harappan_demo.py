"""
Streamlit demo UI for the Universal Translation Engine 0/0.

Shows:
- text → tokens, phonemes, symbolic layer
- (futuro) Harappan sequence → decoded representation
"""

import streamlit as st
from universal_translation.api.translate import translate


st.set_page_config(
    page_title="Universal Translation Engine 0/0 – Demo",
    layout="wide",
)

st.title("Universal Translation Engine 0/0 – Demo")

st.markdown(
    """
    Esta demo mostra a **pipeline simbólica**:

    1. Tokenização  
    2. Fonemas universais  
    3. Anotação simbólica (0/0, numerologia, arquétipos – em construção)
    """
)

text = st.text_area("Digite um texto em qualquer idioma:", "Om Shanti Draconis")

if st.button("Traduzir simbolicamente"):
    if not text.strip():
        st.warning("Por favor, insira um texto.")
    else:
        result = translate(text)
        st.subheader("Tokens")
        st.write(result["tokens"])

        st.subheader("Fonemas universais (placeholder)")
        st.json(result["phonemes"])

        st.subheader("Camada simbólica (0/0 – em evolução)")
        st.json(result["symbolic"])
