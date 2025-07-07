import streamlit as st

def afficher_types_controle():
    st.write("🧪 Types de contrôle à effectuer")

    coffrage = st.checkbox("Coffrage", key="coffrage")
    ferraillage = st.checkbox("Ferraillage", key="ferraillage")
    betonnage = st.checkbox("Bétonnage", key="betonnage")
    #autre = st.checkbox("Autre", key="autre")

    types_controle = []
    if coffrage:
        types_controle.append("Coffrage")
    if ferraillage:
        types_controle.append("Ferraillage")
    if betonnage:
        types_controle.append("Bétonnage")
    #if autre:
     #   types_controle.append("Autre")

    #st.write("Types sélectionnés :", types_controle)
    return types_controle
