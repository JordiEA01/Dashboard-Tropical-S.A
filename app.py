import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- Configuración de la página ----------
st.set_page_config(
    page_title="Dashboard Tropical S.A.",
    layout="wide",
    page_icon="🍍"
)

# ---------- Estilos personalizados ----------
st.markdown("""
    <style>
        body {
            background-color: #f5f9f6;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #f5f9f6;
        }
        h1, h2, h3 {
            color: #2a9d8f;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Encabezado con logo y título ----------
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7e/Costa_Rica_coat_of_arms.svg", width=80)
with col_title:
    st.markdown("## Tropical S.A. – Inteligencia Comercial B2B en Colombia")
    st.markdown("#### Exportación de jugos naturales saludables y sostenibles")
    st.markdown("*Dashboard estratégico con enfoque en relaciones comerciales B2B*")

# ---------- Paleta de colores corporativa ----------
color_1 = '#2a9d8f'  # Verde tropical
color_2 = '#f4a261'  # Naranja suave
color_3 = '#264653'  # Azul oscuro
color_4 = '#e9c46a'  # Amarillo claro

# ---------- Carga de datos ----------
importaciones = pd.read_csv("importaciones.csv")
origenes = pd.read_csv("origenes.csv")
supermercados = pd.read_csv("supermercados.csv")
actores = pd.read_excel("actores_comerciales_colombia.xlsx")
posicionamiento = pd.read_excel("posicionamiento_estrategico_colombia.xlsx")

# ---------- Sección 1: Importaciones ----------
st.markdown("### 📈 1. Evolución de Importaciones de Jugos de Frutas (2021–2023)")
fig1 = px.line(importaciones, x='Año', y='Importaciones (USD millones)', markers=True,
               line_shape="spline", template='plotly_white', color_discrete_sequence=[color_1])
fig1.update_layout(title="Tendencia de importaciones de jugo en Colombia", xaxis_title="Año", yaxis_title="Millones USD")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# ---------- Sección 2: Principales países de origen ----------
st.markdown("### 🌎 2. Origen de Jugos Importados")
fig2 = px.bar(origenes, x='País', y='Valor (USD millones)', color='País',
              template='plotly_white', color_discrete_sequence=px.colors.sequential.Teal)
fig2.update_layout(title="Principales países exportadores de jugo hacia Colombia")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ---------- Sección 3: Supermercados potenciales ----------
st.markdown("### 🛒 3. Presencia de Cadenas de Supermercados en Colombia")
fig3 = px.pie(supermercados, names='Cadena', values='Puntos de venta',
              template='plotly_white', color_discrete_sequence=[color_1, color_2, color_3])
fig3.update_layout(title="Cobertura geográfica de cadenas clave")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# ---------- Sección 4: Actores comerciales identificados ----------
st.markdown("### 🤝 4. Actores Comerciales Identificados")
st.dataframe(actores, use_container_width=True)

st.markdown("---")

# ---------- Sección 5: Posicionamiento estratégico ----------
st.markdown("### 📌 5. Posicionamiento Estratégico")
fig5 = px.scatter(posicionamiento, x='Impacto Comercial', y='Nivel de Alianza',
                  size='Potencial', color='Actor',
                  template='plotly_white', color_discrete_sequence=px.colors.qualitative.Bold)
fig5.update_layout(title="Mapa de posicionamiento de actores estratégicos")
st.plotly_chart(fig5, use_container_width=True)
