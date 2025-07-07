import streamlit as st

def controle_fait(type_controle):
    for key, val in st.session_state.items():
        if key.startswith(type_controle) and val:  # val est True => case cochée
            return "Oui"
    return "Non"