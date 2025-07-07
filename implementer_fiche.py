import json

st.write("--- Début de impl_fiche.py ---")

def implementer_num_fiche(nouveau_num, chantier_nom, data):
    data[chantier_nom]["nb_fiches"] = nouveau_num
    # Facultatif : enregistrer dans le fichier si tu veux que ça persiste
    with open("chantiers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
