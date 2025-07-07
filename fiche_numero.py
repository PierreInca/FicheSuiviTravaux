import streamlit as st
from datetime import datetime
from types_controle import afficher_types_controle

def gerer_numero_fiche(data):
    """
    Affiche la date du jour, gère le numéro de fiche, et demande les informations liées au contrôle.
        """

    # Date du jour
    date_du_jour = datetime.now().strftime("%d/%m/%Y")
    st.markdown(f"📅 **Date du jour :** `{date_du_jour}`")

    # Numéro suggéré
    nb_fiches = data.get("nb_fiches", 0)
    numero_suggere = int(nb_fiches) + 1
    numero_formate = str(numero_suggere).zfill(3)
    st.markdown(f"### 📄 Numéro suggéré de la fiche : `{numero_formate}`")

    # Entrée manuelle (optionnelle)
    numero_manuel = st.text_input("🔢 Modifier manuellement le numéro de fiche (laisser vide pour utiliser le suggéré)", value="")

    if numero_manuel.strip():
        numero_utilise = numero_manuel.strip().zfill(3)
    else:
        numero_utilise = numero_formate

    st.markdown(f"### ✏️ Numéro utilisé pour cette fiche : `{numero_utilise}`")

    # Demande des informations supplémentaires
    ouvrage = st.text_input("🏗️ Ouvrage concerné", placeholder="Ex : Radier P1, Voile V2, etc.")
    plans_demandes = st.text_area("🗂️ Plans demandés pour le contrôle", placeholder="Ex : Plan 100-VC-201, coupe A-A, etc.")


    # Choix des types de contrôles
    types_controle = afficher_types_controle()


    return numero_utilise, date_du_jour, ouvrage, plans_demandes, types_controle