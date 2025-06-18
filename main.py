import streamlit as st
from pages.aluminium_chart import display_aluminium_chart
from utils import get_chemical_status

st.set_page_config(layout="wide", page_title="Versorgungsrisiko Eloxalbranche")

st.title("Versorgungsrisiko-Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    get_chemical_status("Schwefelsäure")
with col2:
    get_chemical_status("Natronlauge")
with col3:
    get_chemical_status("Aluminium")

st.markdown("---")
st.subheader("Aluminiumnachfrage in Deutschland – IST & Prognose (6 Monate)")
display_aluminium_chart()