import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Alineamiento Dinámico - Huawei",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
    <style>
    .main {padding: 0rem 1rem;}
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #FF0000;
        font-family: 'Helvetica Neue', sans-serif;
        padding-bottom: 20px;
        border-bottom: 3px solid #FF0000;
    }
    h2 {
        color: #333333;
        margin-top: 30px;
        padding-left: 10px;
        border-left: 5px solid #FF0000;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("🎯 Dashboard Ejecutivo: Alineamiento Dinámico")
st.markdown("### Caso de Estudio: Huawei Technologies (1987-2026)")
st.markdown("---")

# Sidebar
st.sidebar.title("⚙️ Panel de Control")
st.sidebar.markdown("---")

vista_seleccionada = st.sidebar.radio(
    "Seleccione Vista:",
    ["📊 Vista Ejecutiva", "🎯 Transición Modelo de Negocio", "🔄 Reestructuración Operativa", 
     "🚀 Superación de Barreras", "🌍 Aprovechamiento Periferia", "⚠️ Análisis de Riesgos"],
    index=0
)

periodo_seleccionado = st.sidebar.select_slider(
    "Período de Análisis:",
    options=["2010", "2015", "2020", "2023", "2024 (Actual)", "2026 (Target)"],
    value="2024 (Actual)"
)

mostrar_competencia = st.sidebar.checkbox("Mostrar Comparativa Competitiva", value=True)

st.sidebar.markdown("---")
st.sidebar.info("""
**Última Actualización:** Febrero 2026  
**Fuente:** Simulación basada en caso de estudio  
**Responsable:** Junta Directiva
""")

# Funciones para generar datos
def generar_datos_ingresos():
    años = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
    ingresos_totales = [60.8, 75.1, 92.5, 107.1, 122.0, 136.7, 113.5, 124.3, 141.2, 148.0, 155.0, 162.0]
    ingresos_digitales = [12.2, 20.3, 31.4, 42.8, 52.5, 61.2, 52.7, 62.1, 76.0, 84.2, 93.0, 104.8]
    porcentaje_digital = [round((d/t)*100, 1) for d, t in zip(ingresos_digitales, ingresos_totales)]
    
    return pd.DataFrame({
        'Año': años,
        'Ingresos Totales (USD B)': ingresos_totales,
        'Ingresos Digitales (USD B)': ingresos_digitales,
        '% Digital': porcentaje_digital
    })

def generar_datos_nps():
    años = [2015, 2018, 2020, 2023, 2024, 2026]
    return pd.DataFrame({
        'Año': años,
        'Tier-1 Desarrollados': [18, 32, 28, 42, 48, 55],
        'Tier-2/3 Emergentes': [45, 58, 54, 67, 72, 75],
        'Enterprise': [22, 35, 31, 48, 52, 60],
        'Consumidores': [38, 52, 48, 61, 65, 70]
    })

def generar_datos_rd():
    años = [2015, 2018, 2020, 2023, 2024, 2026]
    return pd.DataFrame({
        'Año': años,
        'Huawei': [15.1, 14.7, 14.3, 16.6, 17.0, 18.5],
        'Nokia': [8.2, 9.1, 8.8, 9.5, 9.8, 10.2],
        'Ericsson': [11.4, 12.3, 11.9, 12.8, 13.1, 13.5],
        'Samsung': [7.8, 8.5, 8.2, 8.9, 9.2, 9.5],
        'Apple': [4.1, 5.2, 6.8, 7.5, 7.9, 8.2]
    })

def generar_datos_geograficos():
    regiones = ['China', 'Asia-Pacífico', 'Europa', 'Latinoamérica', 'África', 'Middle East', 'Norteamérica']
    return pd.DataFrame({
        'Región': regiones,
        '2010': [72, 8, 11, 4, 3, 2, 0.2],
        '2015': [58, 12, 18, 6, 4, 3, 0.8],
        '2020': [54, 14, 16, 7, 5, 4, 0.5],
        '2024': [46, 17, 21, 9, 7, 6, 0.2],
        '2026 Target': [42, 18, 23, 10, 8, 7, 0.5]
    })

def generar_datos_riesgos():
    return pd.DataFrame({
        'Riesgo': ['Escalada USA-China', 'Fragmentación 5G/6G', 'Obsolescencia Modelos', 
                   'Pérdida Talento', 'Disrupción Tecnológica'],
        'Probabilidad': [75, 50, 25, 40, 45],
        'Impacto': [95, 70, 45, 75, 90],
        'Score': [9.0, 6.5, 3.8, 5.2, 7.2],
        'Estado': ['🔴', '🟡', '🟢', '🟡', '🟡']
    })

# VISTA EJECUTIVA
if vista_seleccionada == "📊 Vista Ejecutiva":
    st.header("📊 Vista Ejecutiva: Semáforo General de Alineamiento Dinámico")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📈 Score Agregado", "85.9 / 100", "+3.2 vs. 2023")
    with col2:
        st.metric("💰 Ingresos Digitales", "56.9%", "+4.1% YoY")
    with col3:
        st.metric("⚡ Time-to-Market", "13 semanas", "-1 semana")
    with col4:
        st.metric("🎯 Claridad Estratégica", "4.5 / 5.0", "+0.1 pts")
    
    st.markdown("---")
    
    st.subheader("🚦 Semáforo de Sub-Objetivos")
    
    sub_objetivos = pd.DataFrame({
        'Sub-Objetivo': ['Transición Modelo Negocio', 'Reestructuración Operativa', 
                         'Superación Barreras Imagen', 'Aprovechamiento Periferia'],
        'Score': [85, 92, 78, 88],
        'Status': ['🟢', '🟢', '🟡', '🟢']
    })
    
    fig_scores = go.Figure()
    colors = ['#00CC66' if s >= 80 else '#FFD700' if s >= 60 else '#FF4444' for s in sub_objetivos['Score']]
    
    fig_scores.add_trace(go.Bar(
        y=sub_objetivos['Sub-Objetivo'],
        x=sub_objetivos['Score'],
        orientation='h',
        marker=dict(color=colors),
        text=sub_objetivos['Score'],
        textposition='outside'
    ))
    
    fig_scores.update_layout(
        title="Performance por Sub-Objetivo (0-100)",
        xaxis_title="Score",
        height=400,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig_scores, use_container_width=True)
    
    st.dataframe(sub_objetivos, use_container_width=True, hide_index=True)

# TRANSICIÓN MODELO DE NEGOCIO
elif vista_seleccionada == "🎯 Transición Modelo de Negocio":
    st.header("🎯 Transición del Modelo de Negocio")
    
    tab1, tab2, tab3 = st.tabs(["📊 Ingresos Digitales", "⚡ Time-to-Market", "😊 NPS"])
    
    with tab1:
        df_ingresos = generar_datos_ingresos()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Ingresos Digitales 2024", "$84.2B", "+10.8% YoY")
        with col2:
            st.metric("% Digital Actual", "56.9%", "+3.1 pp")
        with col3:
            st.metric("Target 2026", "65%", "Gap: -8.1 pp")
        
        fig_ingresos = go.Figure()
        
        fig_ingresos.add_trace(go.Scatter(
            x=df_ingresos['Año'],
            y=df_ingresos['Ingresos Digitales (USD B)'],
            fill='tozeroy',
            name='Ingresos Digitales',
            line=dict(color='#FF0000', width=3)
        ))
        
        fig_ingresos.update_layout(
            title="Evolución de Ingresos Digitales (2015-2026)",
            xaxis_title="Año",
            yaxis_title="Ingresos (USD B)",
            height=450
        )
        
        st.plotly_chart(fig_ingresos, use_container_width=True)
    
    with tab2:
        st.subheader("Reducción del Time-to-Market")
        
        años_ttm = [1999, 2005, 2009, 2015, 2020, 2023, 2024, 2026]
        tiempo = [74, 52, 36, 22, 16, 14, 13, 10]
        
        fig_ttm = go.Figure()
        fig_ttm.add_trace(go.Scatter(
            x=años_ttm, y=tiempo,
            mode='lines+markers',
            line=dict(color='#FF0000', width=3),
            marker=dict(size=10)
        ))
        
        fig_ttm.update_layout(
            title="Evolución del Time-to-Market (1999-2026)",
            xaxis_title="Año",
            yaxis_title="Semanas",
            height=450
        )
        
        st.plotly_chart(fig_ttm, use_container_width=True)
        
        st.success("**Reducción del 82.4%** desde 1999 (74 semanas) hasta 2024 (13 semanas)")
    
    with tab3:
        df_nps = generar_datos_nps()
        
        fig_nps = go.Figure()
        
        colores = ['#FF0000', '#00CC66', '#0066CC', '#FFD700']
        segmentos = ['Tier-1 Desarrollados', 'Tier-2/3 Emergentes', 'Enterprise', 'Consumidores']
        
        for i, segmento in enumerate(segmentos):
            fig_nps.add_trace(go.Scatter(
                x=df_nps['Año'],
                y=df_nps[segmento],
                mode='lines+markers',
                name=segmento,
                line=dict(width=3, color=colores[i])
            ))
        
        fig_nps.update_layout(
            title="Evolución del NPS por Segmento (2015-2026)",
            xaxis_title="Año",
            yaxis_title="NPS Score",
            height=450
        )
        
        st.plotly_chart(fig_nps, use_container_width=True)

# REESTRUCTURACIÓN OPERATIVA
elif vista_seleccionada == "🔄 Reestructuración Operativa":
    st.header("🔄 Reestructuración Operativa")
    
    st.subheader("Tiempo de Toma de Decisiones Estratégicas")
    
    años = [2005, 2011, 2015, 2020, 2024, 2026]
    dias = [89, 52, 28, 34, 12, 7]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=años, y=dias, marker_color='#FF0000', text=dias, textposition='outside'))
    fig.update_layout(title="Reducción del Tiempo de Decisiones (días)", height=400)
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("**Reducción del 86.5%** desde 2005 (89 días) hasta 2024 (12 días)")

# SUPERACIÓN DE BARRERAS
elif vista_seleccionada == "🚀 Superación de Barreras":
    st.header("🚀 Superación de Barreras de Imagen")
    
    tab1, tab2 = st.tabs(["🔬 I+D", "📜 Patentes"])
    
    with tab1:
        df_rd = generar_datos_rd()
        
        if mostrar_competencia:
            fig_rd = go.Figure()
            
            empresas = ['Huawei', 'Ericsson', 'Nokia', 'Samsung', 'Apple']
            colores = ['#FF0000', '#0066CC', '#0099FF', '#4444FF', '#AAAAAA']
            
            for i, empresa in enumerate(empresas):
                fig_rd.add_trace(go.Scatter(
                    x=df_rd['Año'], y=df_rd[empresa],
                    mode='lines+markers',
                    name=empresa,
                    line=dict(width=4 if empresa=='Huawei' else 2, color=colores[i])
                ))
            
            fig_rd.update_layout(
                title="Inversión en I+D (% de Ingresos)",
                height=450
            )
            
            st.plotly_chart(fig_rd, use_container_width=True)
            
            st.success("**Huawei lidera con 17.0%** en 2024 (vs. Nokia 9.8%, Apple 7.9%)")
    
    with tab2:
        st.metric("Total Patentes 2024", "11,801", "+13.1% vs. 2023")
        
        categorias = ['5G/6G', 'IA', 'Cloud', 'IoT', 'Semiconductores', 'Energía', 'Quantum']
        patentes = [3789, 2567, 1398, 1623, 1045, 845, 534]
        
        fig = go.Figure(go.Bar(x=categorias, y=patentes, marker_color='#FF0000'))
        fig.update_layout(title="Distribución de Patentes por Categoría (2024)", height=400)
        
        st.plotly_chart(fig, use_container_width=True)

# APROVECHAMIENTO PERIFERIA
elif vista_seleccionada == "🌍 Aprovechamiento Periferia":
    st.header("🌍 Distribución Geográfica de Ingresos")
    
    df_geo = generar_datos_geograficos()
    
    fig = go.Figure(data=[go.Pie(
        labels=df_geo['Región'],
        values=df_geo['2024'],
        hole=.3
    )])
    
    fig.update_layout(title="Mix Geográfico 2024", height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("**China**: 46% | **Europa**: 21% | **Asia-Pac**: 17% | **Latam**: 9%")

# ANÁLISIS DE RIESGOS
elif vista_seleccionada == "⚠️ Análisis de Riesgos":
    st.header("⚠️ Análisis de Riesgos Estratégicos")
    
    df_riesgos = generar_datos_riesgos()
    
    fig = go.Figure()
    
    colors = ['#FF4444', '#FFD700', '#00CC66', '#FFD700', '#FFD700']
    
    fig.add_trace(go.Scatter(
        x=df_riesgos['Probabilidad'],
        y=df_riesgos['Impacto'],
        mode='markers+text',
        marker=dict(size=df_riesgos['Score']*10, color=colors),
        text=df_riesgos['Riesgo'],
        textposition='top center'
    ))
    
    fig.update_layout(
        title="Matriz de Riesgos: Probabilidad × Impacto",
        xaxis_title="Probabilidad (%)",
        yaxis_title="Impacto (%)",
        height=600,
        xaxis=dict(range=[0, 100]),
        yaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(df_riesgos, use_container_width=True, hide_index=True)
    
    st.error("⚠️ **Riesgo Crítico**: Escalada USA-China (Score: 9.0)")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>Dashboard Ejecutivo - Caso Huawei</strong></p>
    <p>INCAE Business School | Dr. Juan Carlos Barahona</p>
    <p>📊 Datos Simulados | Febrero 2026</p>
</div>
""", unsafe_allow_html=True)
```
