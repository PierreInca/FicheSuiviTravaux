import streamlit as st
import json
import os

DB_FILE = "controleur.json"

def charger_controleur():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def sauvegarder_controleur(controleurs):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(controleurs, f, indent=2, ensure_ascii=False)

def choix_controleur():
    st.subheader("👷 Sélection ou ajout d’un contrôleur")
    data = charger_controleur()

    options = ["➕ Ajouter un nouveau contrôleur"] + list(data.keys())
    selection = st.selectbox("Contrôleur", options)

    if selection == "➕ Ajouter un nouveau contrôleur":
        nouveau_nom = st.text_input("Nom du nouveau contrôleur")

        if st.button("Enregistrer le contrôleur"):
            if nouveau_nom.strip() == "":
                st.error("Le nom du contrôleur ne peut pas être vide.")
            elif nouveau_nom in data:
                st.warning(f"Le contrôleur '{nouveau_nom}' existe déjà.")
            else:
                data[nouveau_nom] = {}
                sauvegarder_controleur(data)
                st.success(f"✅ Contrôleur '{nouveau_nom}' enregistré avec succès.")
                st.session_state["controleur_actif"] = nouveau_nom

    else:
        st.success(f"✅ Contrôleur sélectionné : **{selection}**")
        st.session_state["controleur_actif"] = selection