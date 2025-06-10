import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Dashboard Tropical S.A.", layout="wide")

# Logo y título
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7e/Costa_Rica_coat_of_arms.svg", width=80)
with col_title:
    st.title("Oportunidades de Exportación de Jugos Naturales en Colombia")
    st.markdown("""
    <style> .main { background-color: #f6f9fc; } </style>
    """, unsafe_allow_html=True)

# Cargar datos
importaciones = pd.read_csv("importaciones.csv")
origenes = pd.read_csv("origenes.csv")
supermercados = pd.read_csv("supermercados.csv")
actores = pd.read_excel("actores_comerciales_colombia.xlsx")
posicionamiento = pd.read_excel("posicionamiento_estrategico_colombia.xlsx")

# Colores de gráficas
color_1 = '#2a9d8f'
color_2 = '#e76f51'
color_3 = '#264653'

# Sección 1: Importaciones
st.subheader("📈 1. Evolución de Importaciones de Jugos de Frutas (2021–2023)")
fig1 = px.line(importaciones, x='Año', y='Importaciones (USD millones)', markers=True,
               line_shape="spline", template='plotly_white', color_discrete_sequence=[color_1])


