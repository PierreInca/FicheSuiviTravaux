import streamlit as st
from nouveau_chantier import creer_nouveau_chantier
from chantier_existant import utiliser_chantier_existant
from arreter_app import bouton_arret
from controleur import choix_controleur

st.set_page_config(page_title="Fiche Suivi Travaux", layout="centered")
st.title("Fiche Suivi Travaux")

# Appelle le bouton d'arrêt
bouton_arret()

choix_controleur()

mode = st.radio("Choisir une option :", ["Créer un nouveau chantier", "Utiliser un chantier existant"])

if mode == "Créer un nouveau chantier":
    creer_nouveau_chantier()
elif mode == "Utiliser un chantier existant":
    utiliser_chantier_existant()