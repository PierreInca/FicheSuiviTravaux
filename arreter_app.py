import streamlit as st
import os
import sys
import signal

def bouton_arret():
    if st.button("❌ Arrêter l'application"):
        st.warning("Arrêt de l'application demandé. Le processus Streamlit va être arrêté.")
        # Tuer le processus principal
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)