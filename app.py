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

# CSS personalizado MEJORADO para colores visibles
st.markdown("""
    <style>
    /* Fondo general */
    .main {
        padding: 0rem 1rem;
        background-color: #ffffff;
    }
    
    /* ARREGLO CRÍTICO: Forzar colores en métricas */
    [data-testid="stMetricValue"] {
        color: #FF0000 !important;
        font-size: 2rem !important;
        font-weight: bold !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #333333 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }
    
    [data-testid="stMetricDelta"] {
        color: #00AA00 !important;
    }
    
    /* Contenedor de métricas */
    .stMetric {
        background-color: #f8f9fa !important;
        padding: 20px !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
        border: 1px solid #e0e0e0 !important;
    }
    
    /* Títulos con colores visibles */
    h1 {
        color: #FF0000 !important;
        font-family: 'Helvetica Neue', sans-serif;
        padding-bottom: 20px;
        border-bottom: 3px solid #FF0000;
    }
    
    h2 {
        color: #333333 !important;
        margin-top: 30px;
        padding-left: 10px;
        border-left: 5px solid #FF0000;
    }
    
    h3 {
        color: #555555 !important;
        margin-top: 20px;
    }
    
    /* Tabs con texto visible */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        color: #333333 !important;
        font-weight: 600 !important;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background-color: #FF0000 !important;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] [data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #333333 !important;
    }
    
    /* Tablas con fondo visible */
    .stDataFrame {
        background-color: #ffffff !important;
    }
    
    /* Expanders con texto visible */
    .streamlit-expanderHeader {
        color: #333333 !important;
        background-color: #f0f2f6 !important;
    }
    
    /* Info boxes, warnings, etc. */
    .stAlert {
        color: #333333 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Logo en sidebar (emoji en lugar de imagen)
st.sidebar.markdown("# 📱 HUAWEI")
st.sidebar.markdown("---")

# Título principal
st.title("🎯 Dashboard Ejecutivo: Alineamiento Dinámico")
st.markdown("### Caso de Estudio: Huawei Technologies (1987-2026)")
st.markdown("---")

# Sidebar con controles
st.sidebar.title("⚙️ Panel de Control")

# Selector de vista
vista_seleccionada = st.sidebar.radio(
    "Seleccione Vista:",
    ["📊 Vista Ejecutiva", "🎯 Transición Modelo de Negocio", "🔄 Reestructuración Operativa", 
     "🚀 Superación de Barreras", "🌍 Aprovechamiento Periferia", "⚠️ Análisis de Riesgos"],
    index=0
)

# Selector de período
periodo_seleccionado = st.sidebar.select_slider(
    "Período de Análisis:",
    options=["2010", "2015", "2020", "2023", "2024 (Actual)", "2026 (Target)"],
    value="2024 (Actual)"
)

# Toggle para comparativa competitiva
mostrar_competencia = st.sidebar.checkbox("Mostrar Comparativa Competitiva", value=True)

st.sidebar.markdown("---")
st.sidebar.info("""
**Última Actualización:** Febrero 2026  
**Fuente:** Simulación basada en caso de estudio  
**Responsable:** Junta Directiva
""")

# ==================== FUNCIONES DE DATOS ====================

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

def generar_datos_ttm():
    años = [1999, 2002, 2005, 2009, 2012, 2015, 2018, 2020, 2023, 2024, 2026]
    tiempo_semanas = [74, 65, 52, 36, 28, 22, 18, 16, 14, 13, 10]
    target = [None, 60, 50, 40, 32, 24, 20, 18, 16, 14, 12]
    
    return pd.DataFrame({
        'Año': años,
        'Tiempo Real (semanas)': tiempo_semanas,
        'Target (semanas)': target
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

def generar_datos_patentes():
    categorias = ['5G/6G', 'Inteligencia Artificial', 'Cloud Computing', 
                  'IoT & Sensores', 'Semiconductores', 'Energía & Sostenibilidad', 'Fotónica & Quantum']
    patentes_2024 = [3789, 2567, 1398, 1623, 1045, 845, 534]
    
    return pd.DataFrame({
        'Categoría': categorias,
        'Patentes 2024': patentes_2024,
        'Target 2026': [4200, 3000, 1600, 1850, 1200, 1000, 650]
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

# ==================== VISTA EJECUTIVA ====================

if vista_seleccionada == "📊 Vista Ejecutiva":
    st.header("📊 Vista Ejecutiva: Semáforo General de Alineamiento Dinámico")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📈 Score Agregado", "85.9 / 100", "+3.2 vs. 2023")
    
    with col2:
        st.metric("💰 Ingresos Digitales", "56.9%", "+4.1% YoY")
    
    with col3:
        st.metric("⚡ Time-to-Market", "13 semanas", "-1 semana", delta_color="inverse")
    
    with col4:
        st.metric("🎯 Claridad Estratégica", "4.5 / 5.0", "+0.1 pts")
    
    st.markdown("---")
    
    # Semáforo de sub-objetivos
    st.subheader("🚦 Semáforo de Sub-Objetivos")
    
    sub_objetivos = pd.DataFrame({
        'Sub-Objetivo': ['Transición Modelo Negocio', 'Reestructuración Operativa', 
                         'Superación Barreras Imagen', 'Aprovechamiento Periferia'],
        'Score': [85, 92, 78, 88],
        'Status': ['🟢', '🟢', '🟡', '🟢']
    })
    
    # Gráfico con texto negro visible
    fig_scores = go.Figure()
    colors = ['#00CC66' if s >= 80 else '#FFD700' if s >= 60 else '#FF4444' for s in sub_objetivos['Score']]
    
    fig_scores.add_trace(go.Bar(
        y=sub_objetivos['Sub-Objetivo'],
        x=sub_objetivos['Score'],
        orientation='h',
        marker=dict(color=colors),
        text=sub_objetivos['Score'],
        textposition='outside',
        textfont=dict(size=14, color='#000000')
    ))
    
    fig_scores.update_layout(
        title=dict(text="Performance por Sub-Objetivo (0-100)", font=dict(size=18, color='#333333')),
        xaxis_title="Score",
        xaxis=dict(range=[0, 100]),
        height=400,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#333333')
    )
    
    st.plotly_chart(fig_scores, use_container_width=True)
    
    st.dataframe(sub_objetivos, use_container_width=True, hide_index=True)
    
    st.success("✅ **Performance Excepcional**: Score de 85.9 ubica a Huawei en el top 5% global en alineamiento dinámico")

# ==================== TRANSICIÓN MODELO DE NEGOCIO ====================

elif vista_seleccionada == "🎯 Transición Modelo de Negocio":
    st.header("🎯 Transición del Modelo de Negocio")
    st.markdown("### De Producto-Céntrico a Servicio-Céntrico")
    
    tab1, tab2, tab3 = st.tabs(["📊 Ingresos Digitales", "⚡ Time-to-Market", "😊 NPS"])
    
    with tab1:
        st.subheader("Crecimiento de Ingresos Digitales")
        
        df_ingresos = generar_datos_ingresos()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Ingresos Digitales 2024", "$84.2B", "+10.8% YoY")
        with col2:
            st.metric("% Digital Actual", "56.9%", "+3.1 pp")
        with col3:
            st.metric("Target 2026", "65%", "Gap: -8.1 pp")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_ingresos['Año'],
            y=df_ingresos['Ingresos Digitales (USD B)'],
            fill='tozeroy',
            name='Ingresos Digitales',
            line=dict(color='#FF0000', width=3),
            fillcolor='rgba(255, 0, 0, 0.1)'
        ))
        
        fig.update_layout(
            title=dict(text="Evolución de Ingresos Digitales (2015-2026)", font=dict(color='#333333')),
            xaxis_title="Año",
            yaxis_title="Ingresos (USD B)",
            height=450,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#333333')
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Gauge mejorado
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=56.9,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "% Ingresos Digitales 2024", 'font': {'size': 20, 'color': '#333333'}},
            delta={'reference': 53.8, 'font': {'color': '#00AA00'}},
            number={'font': {'size': 40, 'color': '#FF0000'}},
            gauge={
                'axis': {'range': [None, 100], 'tickcolor': '#333333'},
                'bar': {'color': "#FF0000"},
                'steps': [
                    {'range': [0, 40], 'color': '#FFE6E6'},
                    {'range': [40, 60], 'color': '#FFD9B3'},
                    {'range': [60, 100], 'color': '#CCFFCC'}
                ],
                'threshold': {'line': {'color': "green", 'width': 4}, 'value': 65}
            }
        ))
        
        fig_gauge.update_layout(height=350, paper_bgcolor='white')
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with tab2:
        df_ttm = generar_datos_ttm()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("TTM Actual (2024)", "13 semanas", "-82.4% vs. 1999")
        with col2:
            st.metric("TTM Target (2026)", "10 semanas", "-23.1%")
        with col3:
            st.metric("Mejora Anual", "4.7 sem/año", "Promedio")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_ttm['Año'],
            y=df_ttm['Tiempo Real (semanas)'],
            mode='lines+markers',
            line=dict(color='#FF0000', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title=dict(text="Evolución del Time-to-Market (1999-2026)", font=dict(color='#333333')),
            height=450,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#333333')
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("**Reducción del 82.4%** desde 1999 (74 semanas) hasta 2024 (13 semanas)")
    
    with tab3:
        df_nps = generar_datos_nps()
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Tier-1", "48", "+6")
        with col2:
            st.metric("Tier-2/3", "72", "+5")
        with col3:
            st.metric("Enterprise", "52", "+4")
        with col4:
            st.metric("Consumidores", "65", "+4")
        
        fig = go.Figure()
        colores = ['#FF0000', '#00CC66', '#0066CC', '#FFD700']
        segmentos = ['Tier-1 Desarrollados', 'Tier-2/3 Emergentes', 'Enterprise', 'Consumidores']
        
        for i, seg in enumerate(segmentos):
            fig.add_trace(go.Scatter(
                x=df_nps['Año'],
                y=df_nps[seg],
                mode='lines+markers',
                name=seg,
                line=dict(width=3, color=colores[i])
            ))
        
        fig.update_layout(
            title=dict(text="Evolución del NPS por Segmento", font=dict(color='#333333')),
            height=450,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#333333')
        )
        
        st.plotly_chart(fig, use_container_width=True)

# ==================== OTRAS VISTAS (Resumen) ====================

elif vista_seleccionada == "🔄 Reestructuración Operativa":
    st.header("🔄 Reestructuración Operativa")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tiempo Decisiones 2024", "12 días", "-86.5% vs. 2005")
    with col2:
        st.metric("Target 2026", "7 días", "-41.7%")
    with col3:
        st.metric("% Bottom-Up", "65.1%", "+4 pp")
    
    st.success("✅ Transformación de centralizado (89 días en 2005) a data-driven + IA (12 días en 2024)")

elif vista_seleccionada == "🚀 Superación de Barreras":
    st.header("🚀 Superación de Barreras de Imagen")
    
    df_rd = generar_datos_rd()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("I+D Huawei 2024", "17.0%", "+0.4pp")
    with col2:
        st.metric("Total Patentes", "11,801", "+13.1%")
    with col3:
        st.metric("Brand Score", "83 / 100", "+3 pts")
    
    if mostrar_competencia:
        fig = go.Figure()
        empresas = ['Huawei', 'Ericsson', 'Nokia', 'Samsung', 'Apple']
        colores = ['#FF0000', '#0066CC', '#0099FF', '#4444FF', '#AAAAAA']
        
        for i, emp in enumerate(empresas):
            fig.add_trace(go.Scatter(
                x=df_rd['Año'],
                y=df_rd[emp],
                mode='lines+markers',
                name=emp,
                line=dict(width=4 if emp=='Huawei' else 2, color=colores[i])
            ))
        
        fig.update_layout(
            title=dict(text="Inversión en I+D (% Ingresos)", font=dict(color='#333333')),
            height=450,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#333333')
        )
        
        st.plotly_chart(fig, use_container_width=True)

elif vista_seleccionada == "🌍 Aprovechamiento Periferia":
    st.header("🌍 Distribución Geográfica")
    
    df_geo = generar_datos_geograficos()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("China", "46%", "-6pp")
    with col2:
        st.metric("Europa", "21%", "+5pp")
    with col3:
        st.metric("Emergentes", "22%", "+4pp")
    with col4:
        st.metric("USA", "0.2%", "-0.3pp")
    
    fig = go.Figure(data=[go.Pie(
        labels=df_geo['Región'],
        values=df_geo['2024'],
        hole=.4,
        textfont=dict(size=14, color='white')
    )])
    
    fig.update_layout(
        title=dict(text="Mix Geográfico 2024", font=dict(color='#333333')),
        height=500,
        paper_bgcolor='white',
        font=dict(color='#333333')
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif vista_seleccionada == "⚠️ Análisis de Riesgos":
    st.header("⚠️ Análisis de Riesgos Estratégicos")
    
    df_riesgos = generar_datos_riesgos()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Riesgos Críticos", "2", "🔴")
    with col2:
        st.metric("Riesgos Medios", "2", "🟡")
    with col3:
        st.metric("Riesgos Bajos", "1", "🟢")
    with col4:
        st.metric("Score Promedio", "6.3 / 10", "Medio-Alto")
    
    fig = go.Figure()
    colors = ['#FF4444', '#FFD700', '#00CC66', '#FFD700', '#FFD700']
    
    fig.add_trace(go.Scatter(
        x=df_riesgos['Probabilidad'],
        y=df_riesgos['Impacto'],
        mode='markers+text',
        marker=dict(size=df_riesgos['Score']*10, color=colors),
        text=df_riesgos['Riesgo'],
        textposition='top center',
        textfont=dict(size=10, color='#333333')
    ))
    
    fig.update_layout(
        title=dict(text="Matriz de Riesgos", font=dict(color='#333333')),
        xaxis_title="Probabilidad (%)",
        yaxis_title="Impacto (%)",
        height=600,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#333333')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(df_riesgos, use_container_width=True, hide_index=True)
    
    st.error("⚠️ **Riesgo Crítico**: Escalada USA-China (Score: 9.0) - Requiere atención máxima de la Junta")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #333333; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
    <p style='font-size: 18px; font-weight: bold; color: #FF0000;'>📊 Dashboard Ejecutivo - Caso Huawei</p>
    <p style='font-size: 14px;'><strong>INCAE Business School</strong> | Dr. Juan Carlos Barahona</p>
    <p style='font-size: 12px; color: #666666;'>Datos Simulados con Fines Académicos | Febrero 2026</p>
    <p style='font-size: 11px; color: #999999; margin-top: 10px;'>
        <em>"La transformación no es un destino tecnológico, sino un flujo ininterrumpido de conversaciones"</em>
    </p>
</div>
""", unsafe_allow_html=True)
