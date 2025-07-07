import streamlit as st
import json
import os

st.write("--- nouv chantier.py ---")

DB_FILE = "chantiers.json"

def charger_chantiers():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def sauvegarder_chantiers(chantiers):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(chantiers, f, indent=2, ensure_ascii=False)

def creer_nouveau_chantier():
    st.subheader("Créer un nouveau chantier")
    chantiers = charger_chantiers()

    nom = st.text_input("Nom du chantier (ex: Howald - Lot 2b)")
    num_chantier = st.text_input("Numéro de chantier")
    designation = st.text_input("Désignation complète du projet")
    mo = st.text_input("Maître d'ouvrage du projet")


    if st.button("Enregistrer le chantier"):
        if nom.strip() == "" or num_chantier.strip() == "":
            st.error("Le nom et le numéro de chantier sont obligatoires.")
        elif nom in chantiers:
            st.warning(f"Le chantier '{nom}' existe déjà.")
        else:
            chantiers[nom] = {
                "num_chantier": num_chantier.strip(),
                "designation": designation.strip(),
                "mo" : mo.strip(),
                "nb_fiches" : 0
            }
            sauvegarder_chantiers(chantiers)
            st.success(f"✅ Chantier '{nom}' enregistré avec succès.")
