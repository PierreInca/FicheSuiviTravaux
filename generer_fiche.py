from datetime import datetime
from docx import Document
from controle_bool import controle_fait
import json
import os
import streamlit as st
from remplir_word import remplacer_champs_dans_doc


DB_FILE = "chantiers.json"
MODELE_FICHE = "suivi_test_2.docx"


def generer_fiche_test(nom_chantier,donnees):
    # Charger les données du JSON
    if not os.path.exists(DB_FILE):
        raise FileNotFoundError(f"Fichier {DB_FILE} introuvable.")

    with open(DB_FILE, "r", encoding="utf-8") as f:
        chantiers = json.load(f)

    if nom_chantier not in chantiers:
        raise ValueError(f"Chantier '{nom_chantier}' introuvable.")

    data = chantiers[nom_chantier]


    # Préparer les données à injecter dans le Word
    champs = {
        "{{rem_gen}}" : st.session_state.get("rem_gen",""),
        "{{projet1}}": nom_chantier,
        "{{mo}}": data.get("mo", "Non précisé"),
        "{{num_chantier}}": data.get("num_chantier", ""),
        "{{designation}}": data.get("designation", ""),
        "{{date}}": datetime.today().strftime("%d/%m/%Y"),
        "{{num_fiche}}": donnees[0],
        "{{ouvrage}}" : donnees[2],
        "{{plans}}" : donnees[3],

        "{{coffrage_oui_non}}" : controle_fait("coffrage"),
        "{{cof_date}}" : st.session_state.get("coffrage_date",""),
        "{{cof_implantation}}" : st.session_state.get("coffrage_implantation",""),
        "{{cof_implantation_obs}}": st.session_state.get("coffrage_implantation_obs",""),
        "{{cof_reservations}}": st.session_state.get("coffrage_réservations",""),
        "{{cof_reservations_obs}}": st.session_state.get("coffrage_réservations_obs",""),
        "{{cof_peaux}}": st.session_state.get("coffrage_peau_de_coffrage",""),
        "{{cof_peaux_obs}}": st.session_state.get("coffrage_peau_de_coffrage_obs",""),
        "{{cof_rmq}}": st.session_state.get("coffrage_obs", ""),

        "{{ferraillage_oui_non}}" : controle_fait("ferraillage"),
        "{{fer_date}}": st.session_state.get("ferraillage_date",""),
        "{{fer_conf_plan}}": st.session_state.get("ferraillage_conformité_du_plan",""),
        "{{fer_conf_plan_obs}}": st.session_state.get("ferraillage_conformité_du_plan_obs", ""),
        "{{fer_calage}}": st.session_state.get("ferraillage_calage_et_écarteur",""),
        "{{fer_calage_obs}}": st.session_state.get("ferraillage_calage_et_écarteur_obs", ""),
        "{{fer_enrobage}}": st.session_state.get("ferraillage_enrobage",""),
        "{{fer_enrobage_obs}}": st.session_state.get("ferraillage_enrobage_obs", ""),
        "{{fer_rec}}": st.session_state.get("ferraillage_recouvrement",""),
        "{{fer_rec_obs}}": st.session_state.get("ferraillage_recouvrement_obs", ""),
        "{{fer_rmq}}": st.session_state.get("ferraillage_obs", ""),

        "{{bétonnage_oui_non}}": controle_fait("betonnage"),
        "{{bet_date}}": st.session_state.get("bétonnage_date",""),
        "{{bet_controle_BL}}": st.session_state.get("bétonnage_contrôle_bon_de_livraison", ""),
        "{{bet_controle_BL_obs}}": st.session_state.get("bétonnage_contrôle_bon_de_livraison_obs", ""),
        "{{bet_matériel}}": st.session_state.get("bétonnage_matériel_de_mise_en_oeuvre", ""),
        "{{bet_matériel_obs}}": st.session_state.get("bétonnage_matériel_de_mise_en_oeuvre_obs", ""),
        "{{bet_enrobage}}": st.session_state.get("bétonnage_enrobage",""),
        "{{bet_enrobage_obs}}": st.session_state.get("bétonnage_enrobage_obs", ""),
        "{{bet_rmq}}": st.session_state.get("bétonnage_obs", ""),

        "{{controleur}}" : st.session_state.get("controleur_actif","")

    }
    st.write("Données à injecter dans Word :", champs)
    # Charger le modèle Word
    doc = Document(MODELE_FICHE)

    remplacer_champs_dans_doc(doc, champs)

    # Enregistrer le nouveau fichier Word
    nom_sortie = os.path.abspath(f"Fiche_TEST_{nom_chantier.replace(' ', '_')}.docx")
    doc.save(nom_sortie)
    return nom_sortie

