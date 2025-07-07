import streamlit as st

# Éléments à contrôler pour le betonnage
elements_betonnage = ["Contrôle bon de livraison", "Matériel de mise en oeuvre", "Enrobage"]

def afficher_fenetre_betonnage():
    with st.expander("🪵 Contrôle : Bétonnage"):

        st.text_area("📅 Date du contrôle", key="betonnage_date")

        for element in elements_betonnage:
            st.subheader(f"🔎 Élément à contrôler : {element}")

            # Define the options with the values you want to store
            status_options = {
                "Conforme (C)": "Conforme",
                "A mettre en conformité (AC)": "A mettre en conformité",
                "Non-conforme (NC)": "Non-conforme"
            }
            # The display options for the user
            display_options = list(status_options.keys())

            # The key for this specific element's status
            element_status_key = f"bétonnage_{element.lower().replace(' ', '_')}"

            status_selection_label = st.radio(
                "Statut",
                options=display_options,
                index=None,  # No default selection
                key=f"{element_status_key}_radio",  # Unique key for the radio button widget
                horizontal=True
            )

            # Store the actual desired value (e.g., "Conforme") directly
            if status_selection_label:
                st.session_state[element_status_key] = status_options[status_selection_label]
            else:
                st.session_state[element_status_key] = None  # Or an empty string if nothing selected

            # Store observations with a clear key
            st.text_area("Observations", key=f"{element_status_key}_obs")

            st.markdown("---")

            # A vérifier pour que le statut sera bien extrait