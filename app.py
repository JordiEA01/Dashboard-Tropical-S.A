import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Tropical S.A.", layout="wide")
st.title("Oportunidades de Exportación de Jugos Naturales en Colombia")

# Cargar datos desde archivos CSV
importaciones = pd.read_csv("importaciones.csv")
origenes = pd.read_csv("origenes.csv")
supermercados = pd.read_csv("supermercados.csv")

# Sección 1: Importaciones de Jugos de Frutas
st.subheader("Importaciones de Jugos de Frutas (2021–2023)")
fig1 = px.line(importaciones, x='Año', y='Importaciones (USD millones)', markers=True)
st.plotly_chart(fig1, use_container_width=True)

# Sección 2: Principales Orígenes de Importación
st.subheader("Principales Orígenes de Importación (2023)")
fig2 = px.bar(origenes, x='Importaciones (USD millones)', y='País', orientation='h')
st.plotly_chart(fig2, use_container_width=True)

# Sección 3: Población Total y Segmento Saludable
st.subheader("Población Total y Segmento Saludable")
total_population = 53.26
healthy_segment = total_population * 0.40
col1, col2 = st.columns(2)
col1.metric("Población Total (2025)", f"{total_population:.2f} millones")
col2.metric("Segmento Saludable (40%)", f"{healthy_segment:.2f} millones")

# Sección 4: Cadenas de Supermercados
st.subheader("Cadenas de Supermercados y Tiendas de Descuento")
fig3 = px.bar(supermercados, x='Cadena', y='Número de Tiendas')
st.plotly_chart(fig3, use_container_width=True)

# Sección 5: Participación en Ferias Comerciales
st.subheader("Participación en Ferias Comerciales y Networking Profesional")
st.markdown("""
- **Bioexpo 2023**: Más de 31 acuerdos comerciales por un valor de 10,112 millones de pesos.
""")

