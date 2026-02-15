import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Configuración
st.set_page_config(
    page_title="Dashboard Huawei",
    page_icon="🎯",
    layout="wide"
)

# CSS para arreglar colores
st.markdown("""
    <style>
    .main {padding: 0rem 1rem;}
    
    /* Arreglar el color de las métricas */
    [data-testid="stMetricValue"] {
        color: #FF0000 !important;
        font-size: 2rem !important;
        font-weight: bold !important;
    }
    
    [data-testid="stMetricDelta"] {
        color: #00CC66 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #333333 !important;
        font-weight: 600 !important;
    }
    
    /* Títulos */
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
    
    h3 {
        color: #666666;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }
    </style>
""", unsafe_allow_html=True)

# Logo en sidebar (usando emoji en lugar de imagen)
st.sidebar.markdown("# 📱 HUAWEI")
st.sidebar.markdown("---")

# Título principal
st.title("🎯 Dashboard Ejecutivo: Alineamiento Dinámico")
st.markdown("### Caso de Estudio: Huawei Technologies (1987-2026)")
st.markdown("---")

# Sidebar
st.sidebar.title("⚙️ Panel de Control")
vista = st.sidebar.radio(
    "Seleccione Vista:",
    ["📊 Vista Ejecutiva", "💰 Ingresos Digitales", "🔬 I+D Competitivo", "🌍 Distribución Geográfica"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Última Actualización:** Febrero 2026  
**Fuente:** Caso de estudio INCAE  
**Responsable:** Junta Directiva
""")

# VISTA EJECUTIVA
if vista == "📊 Vista Ejecutiva":
    st.header("📊 Vista Ejecutiva: Semáforo General")
    
    # Métricas principales con colores visibles
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📈 Score Agregado",
            value="85.9 / 100",
            delta="+3.2 vs. 2023"
        )
    
    with col2:
        st.metric(
            label="💰 Ingresos Digitales",
            value="56.9%",
            delta="+4.1% YoY"
        )
    
    with col3:
        st.metric(
            label="⚡ Time-to-Market",
            value="13 semanas",
            delta="-1 semana",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            label="🎯 Claridad Estratégica",
            value="4.5 / 5.0",
            delta="+0.1 pts"
        )
    
    st.markdown("---")
    
    # Semáforo
    st.subheader("🚦 Semáforo de Sub-Objetivos")
    
    sub_objetivos = pd.DataFrame({
        'Sub-Objetivo': ['Transición Modelo Negocio', 'Reestructuración Operativa', 
                         'Superación Barreras Imagen', 'Aprovechamiento Periferia'],
        'Score': [85, 92, 78, 88],
        'Status': ['🟢', '🟢', '🟡', '🟢']
    })
    
    fig = go.Figure(go.Bar(
        y=sub_objetivos['Sub-Objetivo'],
        x=sub_objetivos['Score'],
        orientation='h',
        marker_color=['#00CC66', '#00CC66', '#FFD700', '#00CC66'],
        text=sub_objetivos['Score'],
        textposition='outside',
        textfont=dict(size=14, color='black')
    ))
    
    fig.update_layout(
        title="Performance por Sub-Objetivo (0-100)",
        xaxis_title="Score",
        height=400,
        xaxis=dict(range=[0, 100]),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabla con colores
    st.dataframe(
        sub_objetivos.style.set_properties(**{
            'background-color': '#f0f2f6',
            'color': '#333333',
            'border-color': '#cccccc'
        }),
        hide_index=True,
        use_container_width=True
    )
    
    st.success("✅ **Performance Excepcional**: Score de 85.9 ubica a Huawei en el top 5% global")

# INGRESOS DIGITALES
elif vista == "💰 Ingresos Digitales":
    st.header("💰 Evolución de Ingresos Digitales")
    
    años = list(range(2015, 2027))
    ingresos_digitales = [12.2, 20.3, 31.4, 42.8, 52.5, 61.2, 52.7, 62.1, 76.0, 84.2, 93.0, 104.8]
    porcentaje = [20.1, 27.0, 33.9, 40.0, 43.0, 44.8, 46.4, 50.0, 53.8, 56.9, 60.0, 64.7]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Ingresos 2024", "$84.2B", "+10.8%")
    with col2:
        st.metric("% Digital", "56.9%", "+3.1pp")
    with col3:
        st.metric("Target 2026", "65%", "-8.1pp gap")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=años, 
        y=ingresos_digitales,
        mode='lines+markers',
        name='Ingresos Digitales',
        line=dict(color='#FF0000', width=3),
        fill='tozeroy',
        fillcolor='rgba(255, 0, 0, 0.1)',
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title="Ingresos Digitales (USD Billones)",
        xaxis_title="Año",
        yaxis_title="Ingresos (USD B)",
        height=450,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#333333')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Gauge con colores visibles
    fig2 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=56.9,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "% Ingresos Digitales 2024", 'font': {'size': 20, 'color': '#333333'}},
        delta={'reference': 53.8, 'font': {'size': 16, 'color': '#00CC66'}},
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
    
    fig2.update_layout(height=350, paper_bgcolor='white')
    st.plotly_chart(fig2, use_container_width=True)
    
    st.info("🎯 **OKR Cumplido**: Incrementar ventas digitales al 40% en 2 años → Alcanzado 56.9% en 2024")

# I+D COMPETITIVO
elif vista == "🔬 I+D Competitivo":
    st.header("🔬 Inversión en I+D (% de Ingresos)")
    
    años = [2015, 2018, 2020, 2023, 2024, 2026]
    
    data = {
        'Huawei': [15.1, 14.7, 14.3, 16.6, 17.0, 18.5],
        'Ericsson': [11.4, 12.3, 11.9, 12.8, 13.1, 13.5],
        'Nokia': [8.2, 9.1, 8.8, 9.5, 9.8, 10.2],
        'Samsung': [7.8, 8.5, 8.2, 8.9, 9.2, 9.5],
        'Apple': [4.1, 5.2, 6.8, 7.5, 7.9, 8.2]
    }
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Huawei (2024)", "17.0%", "+0.4pp YoY")
    with col2:
        st.metric("vs. Nokia", "+73.5%", "Brecha amplia")
    with col3:
        st.metric("vs. Apple", "+115%", "Más del doble")
    
    fig = go.Figure()
    
    colores = {
        'Huawei': '#FF0000', 
        'Ericsson': '#0066CC', 
        'Nokia': '#0099FF', 
        'Samsung': '#4444FF', 
        'Apple': '#999999'
    }
    
    for empresa, valores in data.items():
        fig.add_trace(go.Scatter(
            x=años, y=valores,
            mode='lines+markers',
            name=empresa,
            line=dict(width=4 if empresa=='Huawei' else 2, color=colores[empresa]),
            marker=dict(size=12 if empresa=='Huawei' else 8)
        ))
    
    fig.update_layout(
        title="Comparativa de Inversión en I+D vs. Competencia",
        xaxis_title="Año",
        yaxis_title="% de Ingresos",
        height=500,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#333333'),
        legend=dict(font=dict(size=12, color='#333333'))
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("🏆 **Liderazgo Indiscutido**: Huawei invierte 17.0% (2024) - Duplica a Nokia y triplica a Apple")
    
    # Tabla comparativa con estilos
    comparativa = pd.DataFrame({
        'Empresa': list(data.keys()),
        'I+D 2024 (%)': [data[e][-2] for e in data.keys()]
    }).sort_values('I+D 2024 (%)', ascending=False)
    
    st.dataframe(
        comparativa.style.highlight_max(axis=0, color='#FFE6E6'),
        hide_index=True,
        use_container_width=True
    )

# DISTRIBUCIÓN GEOGRÁFICA
else:
    st.header("🌍 Distribución Geográfica de Ingresos")
    
    regiones = ['China', 'Europa', 'Asia-Pacífico', 'Latinoamérica', 'África', 'Middle East', 'Norteamérica']
    ingresos_2024 = [46, 21, 17, 9, 7, 6, 0.2]
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("China", "46%", "-6pp vs 2020")
    with col2:
        st.metric("Europa", "21%", "+5pp vs 2020")
    with col3:
        st.metric("Emergentes", "22%", "+4pp vs 2020")
    with col4:
        st.metric("Norteamérica", "0.2%", "-0.3pp (sanciones)")
    
    fig = go.Figure(data=[go.Pie(
        labels=regiones,
        values=ingresos_2024,
        hole=.4,
        marker_colors=['#FF0000', '#0066CC', '#00CC66', '#FFD700', '#FF9900', '#9966CC', '#CCCCCC'],
        textfont=dict(size=14, color='white'),
        textposition='inside'
    )])
    
    fig.update_layout(
        title=dict(text="Mix Geográfico de Ingresos 2024", font=dict(size=20, color='#333333')),
        height=500,
        paper_bgcolor='white',
        showlegend=True,
        legend=dict(font=dict(size=12, color='#333333'))
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
    **📊 Estrategia "Periferia → Centro" (1987-2024)**:
    
    - ✅ **Fase 1 (1997-2005)**: Dominio China rural
    - ✅ **Fase 2 (2006-2012)**: Penetración emergentes (Rusia, África, Latam)
    - ✅ **Fase 3 (2013-2019)**: Asalto a desarrollados (Europa)
    - ✅ **Fase 4 (2020-presente)**: Consolidación post-sanciones
    
    **Resultados**:
    - Reducción dependencia China: 72% (2010) → 46% (2024) = **-26 pp**
    - Fortalecimiento Europa: 11% (2010) → 21% (2024) = **+10 pp**
    - Consolidación emergentes: 9% (2010) → 22% (2024) = **+13 pp**
    """)

# Footer con colores visibles
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666666; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
    <p style='font-size: 18px; font-weight: bold; color: #FF0000;'>📊 Dashboard Ejecutivo - Caso Huawei</p>
    <p style='font-size: 14px; color: #333333;'><strong>INCAE Business School</strong> | Dr. Juan Carlos Barahona</p>
    <p style='font-size: 12px; color: #666666;'>Datos Simulados con Fines Académicos | Febrero 2026</p>
    <p style='font-size: 11px; color: #999999; margin-top: 10px;'>
        <em>"La transformación no es un destino tecnológico, sino un flujo ininterrumpido de conversaciones"</em>
    </p>
</div>
""", unsafe_allow_html=True)
