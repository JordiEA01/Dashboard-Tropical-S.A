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

# Colores de gráficas
color_1 = '#2a9d8f'
color_2 = '#e76f51'
color_3 = '#264653'

# Sección 1: Importaciones
st.subheader("1. Evolución de Importaciones de Jugos de Frutas (2021–2023)")
fig1 = px.line(importaciones, x='Año', y='Importaciones (USD millones)', markers=True,
               line_shape="spline", template='plotly_white', color_discrete_sequence=[color_1])
fig1.update_layout(title_text='Tendencia de Importaciones', title_x=0.5)
st.plotly_chart(fig1, use_container_width=True)

# Sección 2: Orígenes
st.subheader("2. Principales Países de Origen de Importación (2023)")
fig2 = px.bar(origenes, x='Importaciones (USD millones)', y='País', orientation='h',
              color_discrete_sequence=[color_2], template='plotly_white')
fig2.update_layout(title_text='Ranking de Países Proveedores', title_x=0.5)
st.plotly_chart(fig2, use_container_width=True)

# Sección 3: Datos demográficos
st.subheader("3. Población y Segmento Saludable")
total_population = 53.26
healthy_segment = total_population * 0.40
col1, col2 = st.columns(2)
col1.metric("Población Total (2025)", f"{total_population:.2f} millones")
col2.metric("Segmento Saludable (40%)", f"{healthy_segment:.2f} millones")

# Sección 4: Supermercados
st.subheader("4. Cadenas de Supermercados y Tiendas de Descuento")
fig3 = px.bar(supermercados, x='Cadena', y='Número de Tiendas',
              color='Cadena', color_discrete_sequence=px.colors.qualitative.Pastel,
              template='plotly_white')
fig3.update_layout(title_text='Presencia Territorial de Supermercados', title_x=0.5)
st.plotly_chart(fig3, use_container_width=True)

# Sección 5: Ferias Comerciales
st.subheader("5. Participación en Ferias Comerciales y Networking Profesional")
with st.container():
    st.markdown("""
    - 🌿 **Bioexpo 2023**: Más de 31 acuerdos comerciales alcanzados por un valor de **10,112 millones de pesos colombianos**.
    - 🌺 **Agroexpo**: Espacio clave para networking con distribuidores, supermercados y canal HORECA.
    - 🌟 **Estrategia**: Posicionamiento de Tropical S.A. como proveedor sostenible y de valor agregado.
    """)

# Estilo adicional
st.markdown("""
<style>
    h1, h2, h3 { color: #264653; }
    .stMetricValue { font-size: 28px; }
    .block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

