import streamlit as st
import datetime

def get_chemical_status(name):
    daten = {
        "Status": "Kritisch" if name == "Aluminium" else "Stabil",
        "Trend": "Fallend" if name == "Aluminium" else "Stabil",
        "Engpassrisiko": "Hoch" if name == "Aluminium" else "Gering",
        "Grund": "Weltweite Nachfrage + Exportbeschränkungen" if name == "Aluminium" else "Aktuell stabile Lage",
        "Letzte Aktualisierung": datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    }

    farbe = "red" if daten["Engpassrisiko"] == "Hoch" else "green"

    st.markdown(
        f'''
        <div style="border:2px solid {farbe}; border-radius:10px; padding:10px; background-color:#f8f9fa">
            <h3>{name}</h3>
            <p><b>Status:</b> {daten['Status']}</p>
            <p><b>Trend:</b> {daten['Trend']}</p>
            <p><b>Engpassrisiko:</b> {daten['Engpassrisiko']}</p>
            <p><b>Grund:</b> {daten['Grund']}</p>
            <p><b>Letzte Aktualisierung:</b> {daten['Letzte Aktualisierung']}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )