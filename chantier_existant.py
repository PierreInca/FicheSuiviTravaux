from fiche_numero import gerer_numero_fiche
from controle_coffrage import afficher_fenetre_coffrage
from controle_ferraillage import afficher_fenetre_ferraillage
from controle_beton import afficher_fenetre_betonnage
from generer_fiche import generer_fiche_test
from implementer_fiche import implementer_num_fiche



import streamlit as st
import json
import os


DB_FILE = "chantiers.json"

def charger_chantiers():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def utiliser_chantier_existant():
    st.subheader("Utiliser un chantier existant")
    chantiers = charger_chantiers()

    if not chantiers:
        st.warning("Aucun chantier enregistré pour le moment.")
        return

    selection = st.selectbox("Sélectionner un chantier", list(chantiers.keys()))
    data = chantiers[selection]

    st.markdown(f"**Numéro :** {data['num_chantier']}")
    st.markdown(f"**Désignation :** {data['designation']}")

    numero, date, ouvrage, plans, types = gerer_numero_fiche(data)
    donnes_controle = [numero,date,ouvrage,plans]

    st.info("⚠️ Données pré-remplies. Tu peux maintenant ajouter les informations spécifiques à la fiche.")


    if "Coffrage" in types:
        afficher_fenetre_coffrage()
    if "Ferraillage" in types:
        afficher_fenetre_ferraillage()
    if "Bétonnage" in types:
        afficher_fenetre_betonnage()

    st.session_state["rem_gen"] = st.radio("Remarque générale", options=["Conforme", "Non conforme"])

    st.markdown("## 🧾 Génération de la fiche PDF")


    if st.button("📝 Générer fiche test"):
        implementer_num_fiche(numero, selection, chantiers)
        fichier = generer_fiche_test(selection, donnes_controle)

        st.write("Valeur de 'fichier' retournée :", fichier)
        st.write("Type de 'fichier' :", type(fichier))

        if isinstance(fichier, str) and os.path.exists(fichier):
            st.success(f"Fiche générée : {fichier}")
            with open(fichier, "rb") as f:
                st.download_button(
                    label="📥 Télécharger la fiche Word",
                    data=f,
                    file_name=os.path.basename(fichier),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        else:
            st.error("❌ Erreur : le fichier Word n'a pas été généré ou le chemin est incorrect.")
