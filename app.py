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

# CSS personalizado para mejorar la estética
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
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
    h3 {
        color: #666666;
        margin-top: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("🎯 Dashboard Ejecutivo: Alineamiento Dinámico")
st.markdown("### Caso de Estudio: Huawei Technologies (1987-2026)")
st.markdown("---")

# Sidebar con controles
st.sidebar.image("https://via.placeholder.com/300x100/FF0000/FFFFFF?text=HUAWEI", use_column_width=True)
st.sidebar.title("⚙️ Panel de Control")
st.sidebar.markdown("---")

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
**Responsable:** Junta Directiva - Office of Strategic Agility
""")

# ==================== DATOS SIMULADOS ====================

# Función para generar datos de ingresos digitales
def generar_datos_ingresos():
    años = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
    ingresos_totales = [60.8, 75.1, 92.5, 107.1, 122.0, 136.7, 113.5, 124.3, 141.2, 148.0, 155.0, 162.0]
    ingresos_digitales = [12.2, 20.3, 31.4, 42.8, 52.5, 61.2, 52.7, 62.1, 76.0, 84.2, 93.0, 104.8]
    porcentaje_digital = [round((d/t)*100, 1) for d, t in zip(ingresos_digitales, ingresos_totales)]
    
    return pd.DataFrame({
        'Año': años,
        'Ingresos Totales (USD B)': ingresos_totales,
        'Ingresos Digitales (USD B)': ingresos_digitales,
        '% Digital': porcentaje_digital,
        'Status': ['🟢' if p >= 50 else '🟡' if p >= 40 else '🔴' for p in porcentaje_digital]
    })

# Función para generar datos de Time-to-Market
def generar_datos_ttm():
    años = [1999, 2002, 2005, 2009, 2012, 2015, 2018, 2020, 2023, 2024, 2026]
    tiempo_semanas = [74, 65, 52, 36, 28, 22, 18, 16, 14, 13, 10]
    target = [None, 60, 50, 40, 32, 24, 20, 18, 16, 14, 12]
    
    return pd.DataFrame({
        'Año': años,
        'Tiempo Real (semanas)': tiempo_semanas,
        'Target (semanas)': target,
        'Reducción %': [None] + [round(((tiempo_semanas[i-1] - tiempo_semanas[i])/tiempo_semanas[i-1])*100, 1) 
                                   for i in range(1, len(tiempo_semanas))]
    })

# Función para generar datos de NPS
def generar_datos_nps():
    años = [2015, 2018, 2020, 2023, 2024, 2026]
    
    return pd.DataFrame({
        'Año': años,
        'Tier-1 Desarrollados': [18, 32, 28, 42, 48, 55],
        'Tier-2/3 Emergentes': [45, 58, 54, 67, 72, 75],
        'Enterprise': [22, 35, 31, 48, 52, 60],
        'Consumidores': [38, 52, 48, 61, 65, 70]
    })

# Función para generar datos de I+D
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

# Función para generar datos de patentes
def generar_datos_patentes():
    categorias = ['5G/6G', 'Inteligencia Artificial', 'Cloud Computing', 
                  'IoT & Sensores', 'Semiconductores', 'Energía & Sostenibilidad', 'Fotónica & Quantum']
    patentes_2024 = [3789, 2567, 1398, 1623, 1045, 845, 534]
    
    return pd.DataFrame({
        'Categoría': categorias,
        'Patentes 2024': patentes_2024,
        'Target 2026': [4200, 3000, 1600, 1850, 1200, 1000, 650]
    })

# Función para generar datos de distribución geográfica
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

# Función para generar datos de riesgos
def generar_datos_riesgos():
    return pd.DataFrame({
        'Riesgo': ['Escalada USA-China', 'Fragmentación 5G/6G', 'Obsolescencia Modelos', 
                   'Pérdida Talento', 'Disrupción Tecnológica'],
        'Probabilidad': [75, 50, 25, 40, 45],
        'Impacto': [95, 70, 45, 75, 90],
        'Score': [9.0, 6.5, 3.8, 5.2, 7.2],
        'Estado': ['🔴', '🟡', '🟢', '🟡', '🟡']
    })

# Función para generar datos de autonomía operativa
def generar_datos_autonomia():
    regiones = ['China HQ', 'Europa', 'Latinoamérica', 'África', 'Asia-Pacífico', 'Middle East', 'Norteamérica']
    
    return pd.DataFrame({
        'Región': regiones,
        '2010': [42, 28, 32, 35, 38, 31, 22],
        '2015': [58, 45, 52, 56, 51, 48, 38],
        '2020': [65, 58, 61, 64, 59, 56, 42],
        '2024': [78, 76, 82, 84, 79, 77, 62],
        '2026 Target': [80, 82, 85, 87, 83, 81, 70]
    })

# ==================== VISTA EJECUTIVA ====================

if vista_seleccionada == "📊 Vista Ejecutiva":
    st.header("📊 Vista Ejecutiva: Semáforo General de Alineamiento Dinámico")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📈 Score Agregado",
            value="85.9 / 100",
            delta="+3.2 vs. 2023",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="💰 Ingresos Digitales",
            value="56.9%",
            delta="+4.1% YoY",
            delta_color="normal"
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
            delta="+0.1 pts",
            delta_color="normal"
        )
    
    st.markdown("---")
    
    # Semáforo de sub-objetivos
    st.subheader("🚦 Semáforo de Sub-Objetivos")
    
    sub_objetivos = pd.DataFrame({
        'Sub-Objetivo': ['Transición Modelo Negocio', 'Reestructuración Operativa', 
                         'Superación Barreras Imagen', 'Aprovechamiento Periferia'],
        'Peso': [30, 25, 25, 20],
        'Score': [85, 92, 78, 88],
        'Status': ['🟢', '🟢', '🟡', '🟢'],
        'Acción Correctiva': [
            'Acelerar en segmento enterprise B2B',
            'Mantener momentum, exportar mejores prácticas',
            'Intensificar comunicación en mercados desarrollados',
            'Blindar posiciones en África/Latam'
        ]
    })
    
    # Gráfico de barras horizontales para scores
    fig_scores = go.Figure()
    
    colors = ['#00CC66' if s >= 80 else '#FFD700' if s >= 60 else '#FF4444' for s in sub_objetivos['Score']]
    
    fig_scores.add_trace(go.Bar(
        y=sub_objetivos['Sub-Objetivo'],
        x=sub_objetivos['Score'],
        orientation='h',
        marker=dict(color=colors),
        text=sub_objetivos['Score'],
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Score: %{x}/100<extra></extra>'
    ))
    
    fig_scores.update_layout(
        title="Performance por Sub-Objetivo (0-100)",
        xaxis_title="Score",
        yaxis_title="",
        height=400,
        showlegend=False,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig_scores, use_container_width=True)
    
    # Tabla de acciones correctivas
    st.dataframe(
        sub_objetivos[['Sub-Objetivo', 'Score', 'Status', 'Acción Correctiva']],
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    
    # Evolución histórica del score agregado
    st.subheader("📈 Evolución Histórica del Score de Alineamiento Dinámico")
    
    años_score = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023, 2024, 2026]
    scores_historicos = [45, 52, 61, 68, 75, 72, 80, 82.7, 85.9, 90]
    
    fig_evolucion = go.Figure()
    
    fig_evolucion.add_trace(go.Scatter(
        x=años_score,
        y=scores_historicos,
        mode='lines+markers',
        name='Score Real',
        line=dict(color='#FF0000', width=3),
        marker=dict(size=10),
        hovertemplate='Año: %{x}<br>Score: %{y}<extra></extra>'
    ))
    
    fig_evolucion.add_hline(y=80, line_dash="dash", line_color="green", 
                            annotation_text="Umbral Excelencia (80)")
    
    fig_evolucion.update_layout(
        title="Trayectoria del Alineamiento Dinámico (2010-2026)",
        xaxis_title="Año",
        yaxis_title="Score Agregado",
        height=400,
        yaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig_evolucion, use_container_width=True)
    
    # Insights clave
    st.info("""
    ### 🎯 Insights Clave:
    
    - **Performance Excepcional**: Score actual de 85.9 ubica a Huawei en el top 5% de empresas globales en alineamiento dinámico
    - **Única Debilidad**: Superación de Barreras de Imagen (78) requiere atención especial en mercados desarrollados
    - **Fortaleza Principal**: Reestructuración Operativa (92) es clase mundial - modelo de referencia para la industria
    - **Trayectoria**: +40.9 puntos desde 2010 (mejora del 90.9%)
    - **Proyección 2026**: Si se mantiene momentum, score alcanzará 90 (excelencia sostenida)
    """)

# ==================== TRANSICIÓN MODELO DE NEGOCIO ====================

elif vista_seleccionada == "🎯 Transición Modelo de Negocio":
    st.header("🎯 Transición del Modelo de Negocio")
    st.markdown("### De Producto-Céntrico a Servicio-Céntrico")
    
    # Tabs para organizar contenido
    tab1, tab2, tab3 = st.tabs(["📊 Ingresos Digitales", "⚡ Time-to-Market", "😊 Satisfacción del Cliente (NPS)"])
    
    with tab1:
        st.subheader("Crecimiento de Ingresos Digitales")
        
        df_ingresos = generar_datos_ingresos()
        
        # Métricas destacadas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Ingresos Digitales 2024", "$84.2B", "+10.8% YoY")
        with col2:
            st.metric("% Digital Actual", "56.9%", "+3.1 pp")
        with col3:
            st.metric("Target 2026", "65%", "Gap: -8.1 pp")
        
        # Gráfico de área apilada
        fig_ingresos = go.Figure()
        
        fig_ingresos.add_trace(go.Scatter(
            x=df_ingresos['Año'],
            y=df_ingresos['Ingresos Digitales (USD B)'],
            fill='tozeroy',
            name='Ingresos Digitales',
            line=dict(color='#FF0000'),
            hovertemplate='Año: %{x}<br>USD: $%{y}B<extra></extra>'
        ))
        
        fig_ingresos.add_trace(go.Scatter(
            x=df_ingresos['Año'],
            y=df_ingresos['Ingresos Totales (USD B)'] - df_ingresos['Ingresos Digitales (USD B)'],
            fill='tonexty',
            name='Ingresos Tradicionales',
            line=dict(color='#CCCCCC'),
            hovertemplate='Año: %{x}<br>USD: $%{y}B<extra></extra>'
        ))
        
        fig_ingresos.update_layout(
            title="Evolución de Ingresos Totales y Digitales (2015-2026)",
            xaxis_title="Año",
            yaxis_title="Ingresos (USD Billones)",
            height=450,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_ingresos, use_container_width=True)
        
        # Gauge chart para % digital
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=56.9,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "% Ingresos Digitales (2024)", 'font': {'size': 24}},
            delta={'reference': 53.8, 'suffix': ' pp vs. 2023'},
            gauge={
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "#FF0000"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 40], 'color': '#FFE6E6'},
                    {'range': [40, 60], 'color': '#FFD9B3'},
                    {'range': [60, 100], 'color': '#CCFFCC'}
                ],
                'threshold': {
                    'line': {'color': "green", 'width': 4},
                    'thickness': 0.75,
                    'value': 65
                }
            }
        ))
        
        fig_gauge.update_layout(height=350)
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        # Tabla de datos
        with st.expander("📋 Ver Datos Detallados"):
            st.dataframe(df_ingresos, use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("Reducción del Time-to-Market")
        
        df_ttm = generar_datos_ttm()
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("TTM Actual (2024)", "13 semanas", "-82.4% vs. 1999")
        with col2:
            st.metric("TTM Target (2026)", "10 semanas", "-23.1% adicional")
        with col3:
            st.metric("Velocidad de Mejora", "4.7 semanas/año", "Promedio 2015-2024")
        
        # Gráfico de líneas con target
        fig_ttm = go.Figure()
        
        fig_ttm.add_trace(go.Scatter(
            x=df_ttm['Año'],
            y=df_ttm['Tiempo Real (semanas)'],
            mode='lines+markers',
            name='Tiempo Real',
            line=dict(color='#FF0000', width=3),
            marker=dict(size=10),
            hovertemplate='Año: %{x}<br>Semanas: %{y}<extra></extra>'
        ))
        
        fig_ttm.add_trace(go.Scatter(
            x=df_ttm['Año'],
            y=df_ttm['Target (semanas)'],
            mode='lines+markers',
            name='Target',
            line=dict(color='#00CC66', width=2, dash='dash'),
            marker=dict(size=8, symbol='diamond'),
            hovertemplate='Año: %{x}<br>Target: %{y}<extra></extra>'
        ))
        
        fig_ttm.update_layout(
            title="Evolución del Time-to-Market (1999-2026)",
            xaxis_title="Año",
            yaxis_title="Tiempo (semanas)",
            height=450,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_ttm, use_container_width=True)
        
        st.success("""
        **🎯 OKR Cumplido**: Reducción del 20% en tiempo de comercialización  
        **Resultado**: De 74 semanas (1999) a 36 semanas (2009) = **-51.4%** (superado ampliamente)  
        **Drivers clave**: Adopción de IPD (Integrated Product Development), metodologías ágiles, y co-creación con clientes
        """)
        
        with st.expander("📋 Ver Datos Detallados"):
            st.dataframe(df_ttm, use_container_width=True, hide_index=True)
    
    with tab3:
        st.subheader("Net Promoter Score (NPS) por Segmento")
        
        df_nps = generar_datos_nps()
        
        # Métricas
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Tier-1 Desarrollados", "48", "+6 vs. 2023")
        with col2:
            st.metric("Tier-2/3 Emergentes", "72", "+5 vs. 2023")
        with col3:
            st.metric("Enterprise", "52", "+4 vs. 2023")
        with col4:
            st.metric("Consumidores", "65", "+4 vs. 2023")
        
        # Gráfico de líneas múltiples
        fig_nps = go.Figure()
        
        colores = ['#FF0000', '#00CC66', '#0066CC', '#FFD700']
        segmentos = ['Tier-1 Desarrollados', 'Tier-2/3 Emergentes', 'Enterprise', 'Consumidores']
        
        for i, segmento in enumerate(segmentos):
            fig_nps.add_trace(go.Scatter(
                x=df_nps['Año'],
                y=df_nps[segmento],
                mode='lines+markers',
                name=segmento,
                line=dict(width=3, color=colores[i]),
                marker=dict(size=10),
                hovertemplate=f'{segmento}<br>Año: %{{x}}<br>NPS: %{{y}}<extra></extra>'
            ))
        
        fig_nps.add_hline(y=50, line_dash="dash", line_color="gray", 
                          annotation_text="Umbral Excelencia (NPS 50)")
        
        fig_nps.update_layout(
            title="Evolución del NPS por Segmento de Cliente (2015-2026)",
            xaxis_title="Año",
            yaxis_title="NPS Score",
            height=450,
            hovermode='x unified',
            yaxis=dict(range=[0, 80])
        )
        
        st.plotly_chart(fig_nps, use_container_width=True)
        
        # Análisis de causalidad
        st.warning("""
        **⚠️ Caída 2020**: Impacto de sanciones USA → pérdida de Google Mobile Services en smartphones  
        **✅ Recuperación 2021-2024**: Pivote hacia HarmonyOS, fortalecimiento en mercados emergentes, mejora en servicio 24/7
        """)
        
        with st.expander("📋 Ver Datos Detallados"):
            st.dataframe(df_nps, use_container_width=True, hide_index=True)

# ==================== REESTRUCTURACIÓN OPERATIVA ====================

elif vista_seleccionada == "🔄 Reestructuración Operativa":
    st.header("🔄 Reestructuración Operativa")
    st.markdown("### De Gobernanza Centralizada a Descentralizada")
    
    tab1, tab2, tab3 = st.tabs(["⚡ Velocidad de Decisiones", "🚀 Iniciativas Bottom-Up", "🌐 Autonomía Regional"])
    
    with tab1:
        st.subheader("Tiempo de Toma de Decisiones Estratégicas")
        
        años_decisiones = [2005, 2009, 2011, 2013, 2015, 2018, 2020, 2022, 2023, 2024, 2026]
        tiempo_dias = [89, 76, 52, 38, 28, 21, 34, 19, 15, 12, 7]
        modelo = ['Centralizado', 'Transición', 'Rotating CEOs', 'Blue/Red Army', 'Descentralizado', 
                  'Empower frontline', 'Crisis', 'Recuperación', 'AI-augmented', 'Data-driven + IA', 'Real-time']
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tiempo Actual (2024)", "12 días", "-86.5% vs. 2005")
        with col2:
            st.metric("Target 2026", "7 días", "-41.7% adicional")
        with col3:
            st.metric("Mejora Anual Promedio", "4.3 días/año", "Último 5 años")
        
        # Gráfico de barras con anotaciones
        fig_decisiones = go.Figure()
        
        colors = ['#FF4444' if d > 50 else '#FFD700' if d > 20 else '#00CC66' for d in tiempo_dias]
        
        fig_decisiones.add_trace(go.Bar(
            x=años_decisiones,
            y=tiempo_dias,
            marker=dict(color=colors),
            text=tiempo_dias,
            textposition='outside',
            hovertemplate='Año: %{x}<br>Días: %{y}<br>Modelo: ' + '<br>'.join([f'{años_decisiones[i]}: {modelo[i]}' for i in range(len(modelo))]) + '<extra></extra>'
        ))
        
        # Añadir anotaciones de hitos
        fig_decisiones.add_annotation(x=2011, y=52, text="Rotating CEOs", showarrow=True, arrowhead=2, arrowcolor="red")
        fig_decisiones.add_annotation(x=2013, y=38, text="Blue/Red Army", showarrow=True, arrowhead=2, arrowcolor="red")
        fig_decisiones.add_annotation(x=2023, y=15, text="AI-augmented", showarrow=True, arrowhead=2, arrowcolor="green")
        
        fig_decisiones.update_layout(
            title="Reducción Dramática del Tiempo de Decisiones Estratégicas (2005-2026)",
            xaxis_title="Año",
            yaxis_title="Tiempo Promedio (días)",
            height=500,
            showlegend=False
        )
        
        st.plotly_chart(fig_decisiones, use_container_width=True)
        
        st.success("""
        **🎯 OKR Cumplido**: Mejorar velocidad de decisiones en 20% en 1 año  
        **Ejemplo 2023 → 2024**: 15 días × 0.80 = 12 días ✅ **ALCANZADO**  
        **Drivers clave**: Rotating CEO system, Blue/Red Army debates, AI-powered scenario planning
        """)
    
    with tab2:
        st.subheader("Iniciativas Impulsadas por Empleados (Bottom-Up)")
        
        años_iniciativas = [2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023, 2024, 2026]
        total_iniciativas = [38, 52, 68, 89, 112, 143, 128, 156, 178, 192, 210]
        iniciativas_bu = [4, 9, 18, 31, 51, 72, 64, 89, 109, 125, 147]
        porcentaje_bu = [round((bu/tot)*100, 1) for bu, tot in zip(iniciativas_bu, total_iniciativas)]
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Iniciativas Bottom-Up 2024", "125", "+14.7% vs. 2023")
        with col2:
            st.metric("% Bottom-Up Actual", "65.1%", "+4 pp YoY")
        with col3:
            st.metric("Inversión Asociada", "$304M", "+13.9% YoY")
        
        # Gráfico de barras apiladas
        fig_iniciativas = go.Figure()
        
        fig_iniciativas.add_trace(go.Bar(
            x=años_iniciativas,
            y=[tot - bu for tot, bu in zip(total_iniciativas, iniciativas_bu)],
            name='Top-Down',
            marker_color='#CCCCCC',
            hovertemplate='Año: %{x}<br>Top-Down: %{y}<extra></extra>'
        ))
        
        fig_iniciativas.add_trace(go.Bar(
            x=años_iniciativas,
            y=iniciativas_bu,
            name='Bottom-Up',
            marker_color='#FF0000',
            hovertemplate='Año: %{x}<br>Bottom-Up: %{y}<extra></extra>'
        ))
        
        fig_iniciativas.update_layout(
            title="Evolución de Iniciativas por Origen (2008-2026)",
            xaxis_title="Año",
            yaxis_title="Número de Iniciativas",
            barmode='stack',
            height=450
        )
        
        st.plotly_chart(fig_iniciativas, use_container_width=True)
        
        # Gráfico de línea para %
        fig_porcentaje = go.Figure()
        
        fig_porcentaje.add_trace(go.Scatter(
            x=años_iniciativas,
            y=porcentaje_bu,
            mode='lines+markers',
            name='% Bottom-Up',
            line=dict(color='#00CC66', width=3),
            marker=dict(size=10),
            fill='tozeroy',
            hovertemplate='Año: %{x}<br>% Bottom-Up: %{y}%<extra></extra>'
        ))
        
        fig_porcentaje.add_hline(y=50, line_dash="dash", line_color="gray", 
                                 annotation_text="Umbral 50% (Cultura de Empoderamiento)")
        
        fig_porcentaje.update_layout(
            title="% de Iniciativas Bottom-Up (Indicador de Cultura de Empoderamiento)",
            xaxis_title="Año",
            yaxis_title="Porcentaje (%)",
            height=400,
            yaxis=dict(range=[0, 100])
        )
        
        st.plotly_chart(fig_porcentaje, use_container_width=True)
        
        st.info("""
        **🎯 Evidencia de Cultura de Empoderamiento Exitosa**:  
        - Promedio de **16 nuevas iniciativas bottom-up/año** desde 2012  
        - 65.1% de todas las iniciativas ahora provienen de la base (vs. 10.5% en 2008)  
        - Inversión asociada creció de $12M (2008) a $304M (2024) = +2,433%
        """)
    
    with tab3:
        st.subheader("Índice de Autonomía Operativa por Región")
        
        df_autonomia = generar_datos_autonomia()
        
        # Mapa de calor
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=df_autonomia[['2010', '2015', '2020', '2024', '2026 Target']].values,
            x=['2010', '2015', '2020', '2024', '2026 Target'],
            y=df_autonomia['Región'],
            colorscale='RdYlGn',
            text=df_autonomia[['2010', '2015', '2020', '2024', '2026 Target']].values,
            texttemplate='%{text}',
            textfont={"size": 12},
            hovertemplate='Región: %{y}<br>Año: %{x}<br>Autonomía: %{z}<extra></extra>'
        ))
        
        fig_heatmap.update_layout(
            title="Evolución de la Autonomía Operativa por Región (0-100)",
            xaxis_title="Período",
            yaxis_title="Región / BU",
            height=500
        )
        
        st.plotly_chart(fig_heatmap, use_container_width=True)
        
        # Gráfico de radar para comparar 2024 vs. 2026
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=df_autonomia['2024'],
            theta=df_autonomia['Región'],
            fill='toself',
            name='2024 Actual',
            line_color='#FF0000'
        ))
        
        fig_radar.add_trace(go.Scatterpolar(
            r=df_autonomia['2026 Target'],
            theta=df_autonomia['Región'],
            fill='toself',
            name='2026 Target',
            line_color='#00CC66',
            line_dash='dash'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100])
            ),
            title="Comparativa: Autonomía Actual (2024) vs. Target (2026)",
            height=500,
            showlegend=True
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
        
        st.warning("""
        **💡 Insight Regional**:  
        - **Fortalezas**: África (84) y Latinoamérica (82) muestran mayor descentralización  
        - **Desafío**: Norteamérica (62) presenta menor autonomía por complejidad regulatoria y sanciones  
        - **Promedio Global**: 77 (vs. 33 en 2010 = +133% de mejora)
        """)

# ==================== SUPERACIÓN DE BARRERAS ====================

elif vista_seleccionada == "🚀 Superación de Barreras":
    st.header("🚀 Superación de Barreras de Imagen")
    st.markdown("### De 'Made in China' a Innovación Pionera (5G)")
    
    tab1, tab2, tab3 = st.tabs(["🔬 Inversión en I+D", "📜 Patentes", "🌟 Brand Perception"])
    
    with tab1:
        st.subheader("Inversión en I+D como % de Ingresos (Comparativa Competitiva)")
        
        df_rd = generar_datos_rd()
        
        if mostrar_competencia:
            # Gráfico de líneas múltiples
            fig_rd = go.Figure()
            
            empresas = ['Huawei', 'Ericsson', 'Nokia', 'Samsung', 'Apple']
            colores = ['#FF0000', '#0066CC', '#0099FF', '#4444FF', '#AAAAAA']
            
            for i, empresa in enumerate(empresas):
                fig_rd.add_trace(go.Scatter(
                    x=df_rd['Año'],
                    y=df_rd[empresa],
                    mode='lines+markers',
                    name=empresa,
                    line=dict(width=4 if empresa == 'Huawei' else 2, color=colores[i]),
                    marker=dict(size=12 if empresa == 'Huawei' else 8),
                    hovertemplate=f'{empresa}<br>Año: %{{x}}<br>I+D: %{{y}}%<extra></extra>'
                ))
            
            fig_rd.update_layout(
                title="Inversión en I+D como % de Ingresos: Huawei vs. Competencia (2015-2026)",
                xaxis_title="Año",
                yaxis_title="% de Ingresos",
                height=500,
                hovermode='x unified',
                yaxis=dict(range=[0, 20])
            )
            
            st.plotly_chart(fig_rd, use_container_width=True)
            
            # Tabla comparativa 2024
            st.subheader("📊 Comparativa 2024")
            
            comparativa_2024 = pd.DataFrame({
                'Empresa': empresas,
                'I+D % Ingresos': [df_rd.iloc[-2][empresa] for empresa in empresas],
                'Gap vs. Huawei': [0] + [df_rd.iloc[-2]['Huawei'] - df_rd.iloc[-2][empresa] for empresa in empresas[1:]]
            })
            comparativa_2024 = comparativa_2024.sort_values('I+D % Ingresos', ascending=False)
            
            st.dataframe(comparativa_2024, use_container_width=True, hide_index=True)
            
            st.success("""
            **🏆 Liderazgo Indiscutido**:  
            - Huawei invierte **17.0%** de ingresos en I+D (2024)  
            - **+73.5%** más que Nokia, su competidor más cercano  
            - **+115%** más que Apple  
            - **+37%** más que Ericsson
            """)
        else:
            # Solo Huawei
            fig_huawei = go.Figure()
            
            fig_huawei.add_trace(go.Scatter(
                x=df_rd['Año'],
                y=df_rd['Huawei'],
                mode='lines+markers',
                name='Huawei',
                line=dict(color='#FF0000', width=4),
                marker=dict(size=12),
                fill='tozeroy',
                hovertemplate='Año: %{x}<br>I+D: %{y}%<extra></extra>'
            ))
            
            fig_huawei.add_hline(y=10, line_dash="dash", line_color="orange", 
                                 annotation_text="Umbral Mínimo Competitivo (10%)")
            
            fig_huawei.add_hline(y=15, line_dash="dash", line_color="green", 
                                 annotation_text="Umbral Liderazgo (15%)")
            
            fig_huawei.update_layout(
                title="Evolución de la Inversión en I+D de Huawei (2015-2026)",
                xaxis_title="Año",
                yaxis_title="% de Ingresos",
                height=450,
                yaxis=dict(range=[0, 20])
            )
            
            st.plotly_chart(fig_huawei, use_container_width=True)
    
    with tab2:
        st.subheader("Registro de Patentes en Tecnologías Emergentes")
        
        df_patentes = generar_datos_patentes()
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Patentes 2024", "11,801", "+13.1% vs. 2023")
        with col2:
            st.metric("Target 2026", "13,500", "+14.4% adicional")
        with col3:
            st.metric("Liderazgo vs. Samsung", "+32.1%", "2nd place")
        
        # Treemap
        fig_treemap = go.Figure(go.Treemap(
            labels=df_patentes['Categoría'],
            parents=[""] * len(df_patentes),
            values=df_patentes['Patentes 2024'],
            text=df_patentes['Patentes 2024'],
            textposition="middle center",
            marker=dict(
                colorscale='Reds',
                cmid=2000
            ),
            hovertemplate='<b>%{label}</b><br>Patentes: %{value}<extra></extra>'
        ))
        
        fig_treemap.update_layout(
            title="Distribución de Patentes por Categoría Tecnológica (2024)",
            height=500
        )
        
        st.plotly_chart(fig_treemap, use_container_width=True)
        
        # Gráfico de barras comparativo 2024 vs. 2026
        fig_patentes_comp = go.Figure()
        
        fig_patentes_comp.add_trace(go.Bar(
            y=df_patentes['Categoría'],
            x=df_patentes['Patentes 2024'],
            name='2024 Actual',
            orientation='h',
            marker_color='#FF0000',
            text=df_patentes['Patentes 2024'],
            textposition='outside'
        ))
        
        fig_patentes_comp.add_trace(go.Bar(
            y=df_patentes['Categoría'],
            x=df_patentes['Target 2026'],
            name='2026 Target',
            orientation='h',
            marker_color='#00CC66',
            text=df_patentes['Target 2026'],
            textposition='outside'
        ))
        
        fig_patentes_comp.update_layout(
            title="Patentes: Actual (2024) vs. Target (2026)",
            xaxis_title="Número de Patentes",
            yaxis_title="",
            height=500,
            barmode='group'
        )
        
        st.plotly_chart(fig_patentes_comp, use_container_width=True)
        
        st.info("""
        **🎯 OKR Cumplido con Creces**:  
        - **Meta Original**: 5,000 patentes/año  
        - **Resultado 2024**: 11,801 patentes (+136% vs. target)  
        - **Líder Absoluto en 5G/6G**: 3,789 patentes (32% del total)  
        - **Apuesta Fuerte en IA**: 2,567 patentes (+20.3% vs. 2023)
        """)
        
        # Benchmark competitivo
        st.subheader("📊 Benchmark Competitivo (Total Patents 2024)")
        
        benchmark_patentes = pd.DataFrame({
            'Empresa': ['Huawei', 'Samsung', 'Qualcomm', 'Ericsson', 'Nokia'],
            'Total Patentes': [11801, 8934, 6712, 5489, 4823],
            'Gap vs. Líder': [0, -2867, -5089, -6312, -6978]
        })
        
        fig_benchmark = go.Figure()
        
        fig_benchmark.add_trace(go.Bar(
            x=benchmark_patentes['Empresa'],
            y=benchmark_patentes['Total Patentes'],
            marker_color=['#FF0000', '#CCCCCC', '#CCCCCC', '#CCCCCC', '#CCCCCC'],
            text=benchmark_patentes['Total Patentes'],
            textposition='outside',
            hovertemplate='%{x}<br>Patentes: %{y}<extra></extra>'
        ))
        
        fig_benchmark.update_layout(
            title="Ranking de Patentes en Telecomunicaciones (2024)",
            xaxis_title="",
            yaxis_title="Total Patentes",
            height=400
        )
        
        st.plotly_chart(fig_benchmark, use_container_width=True)
    
    with tab3:
        st.subheader("Brand Perception Index (0-100)")
        
        dimensiones = ['Calidad Tecnológica', 'Innovación', 'Confianza', 'Sostenibilidad', 'Customer Service', 'Value for Money']
        scores_2024 = [87, 85, 66, 78, 91, 92]
        targets_2026 = [90, 88, 72, 82, 93, 94]
        
        # Gráfico de radar
        fig_brand = go.Figure()
        
        fig_brand.add_trace(go.Scatterpolar(
            r=scores_2024,
            theta=dimensiones,
            fill='toself',
            name='2024 Actual',
            line_color='#FF0000',
            fillcolor='rgba(255, 0, 0, 0.3)'
        ))
        
        fig_brand.add_trace(go.Scatterpolar(
            r=targets_2026,
            theta=dimensiones,
            fill='toself',
            name='2026 Target',
            line_color='#00CC66',
            line_dash='dash',
            fillcolor='rgba(0, 204, 102, 0.2)'
        ))
        
        fig_brand.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100])
            ),
            title="Brand Perception: Análisis Multidimensional",
            height=500,
            showlegend=True
        )
        
        st.plotly_chart(fig_brand, use_container_width=True)
        
        # Métricas clave
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Overall Brand Score", "83 / 100", "+3 vs. 2023")
        with col2:
            st.metric("Fortaleza Principal", "Value for Money: 92", "Mejor en clase")
        with col3:
            st.metric("Desafío Principal", "Confianza: 66", "Gap: -6 vs. target")
        
        # Evolución histórica del Overall Score
        años_brand = [2010, 2015, 2020, 2023, 2024, 2026]
        overall_scores = [55, 68, 66, 80, 83, 87]
        
        fig_evolucion_brand = go.Figure()
        
        fig_evolucion_brand.add_trace(go.Scatter(
            x=años_brand,
            y=overall_scores,
            mode='lines+markers',
            line=dict(color='#FF0000', width=3),
            marker=dict(size=12),
            fill='tozeroy',
            hovertemplate='Año: %{x}<br>Score: %{y}<extra></extra>'
        ))
        
        fig_evolucion_brand.update_layout(
            title="Evolución del Overall Brand Score (2010-2026)",
            xaxis_title="Año",
            yaxis_title="Score",
            height=400,
            yaxis=dict(range=[0, 100])
        )
        
        st.plotly_chart(fig_evolucion_brand, use_container_width=True)
        
        st.warning("""
        **📊 Análisis**:  
        - **Fortalezas**: Customer Service (91), Value for Money (92) - históricamente altos  
        - **Desafíos**: Confianza (66) - impactado por tensiones geopolíticas USA-China  
        - **Progreso**: +28 puntos desde 2010 (+50.9% de mejora)  
        - **Acción Correctiva**: Intensificar campaña de transparencia y contribución social en mercados desarrollados
        """)

# ==================== APROVECHAMIENTO PERIFERIA ====================

elif vista_seleccionada == "🌍 Aprovechamiento Periferia":
    st.header("🌍 Aprovechamiento de la Periferia")
    st.markdown("### Estrategia 'Rurales → Emergentes → Desarrollados'")
    
    tab1, tab2, tab3 = st.tabs(["🗺️ Distribución Geográfica", "📈 Evolución por Región", "🎯 Estrategia de Entrada"])
    
    with tab1:
        st.subheader("Mix Geográfico de Ingresos (%)")
        
        df_geo = generar_datos_geograficos()
        
        # Sankey diagram (simplificado con barras apiladas)
        años_geo = ['2010', '2015', '2020', '2024', '2026 Target']
        
        fig_geo_stack = go.Figure()
        
        regiones = df_geo['Región'].tolist()
        colores_regiones = ['#FF0000', '#FF6666', '#0066CC', '#00CC66', '#FFD700', '#FF9900', '#CCCCCC']
        
        for i, region in enumerate(regiones):
            fig_geo_stack.add_trace(go.Bar(
                name=region,
                x=años_geo,
                y=df_geo[años_geo].iloc[i],
                marker_color=colores_regiones[i],
                hovertemplate=f'{region}<br>%{{x}}: %{{y}}%<extra></extra>'
            ))
        
        fig_geo_stack.update_layout(
            title="Evolución de la Distribución Geográfica de Ingresos (2010-2026)",
            xaxis_title="Período",
            yaxis_title="% de Ingresos Totales",
            barmode='stack',
            height=500,
            yaxis=dict(range=[0, 100])
        )
        
        st.plotly_chart(fig_geo_stack, use_container_width=True)
        
        # Métricas clave
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("China (2024)", "46%", "-6 pp vs. 2020")
        with col2:
            st.metric("Europa (2024)", "21%", "+5 pp vs. 2020")
        with col3:
            st.metric("Latinoamérica (2024)", "9%", "+2 pp vs. 2020")
        with col4:
            st.metric("África (2024)", "7%", "+2 pp vs. 2020")
        
        # Gráfico de torta 2024
        fig_pie = go.Figure(data=[go.Pie(
            labels=df_geo['Región'],
            values=df_geo['2024'],
            marker=dict(colors=colores_regiones),
            hovertemplate='%{label}<br>%{value}% de ingresos<extra></extra>'
        )])
        
        fig_pie.update_layout(
            title="Distribución Geográfica Actual (2024)",
            height=450
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
        
        st.info("""
        **💡 Insight Estratégico**:  
        - **Reducción Dependencia China**: De 72% (2010) a 46% (2024) = -26 pp  
        - **Fortalecimiento Europa**: De 11% (2010) a 21% (2024) = +10 pp  
        - **Consolidación Emergentes**: Latam + África + Middle East = 22% (vs. 9% en 2010)  
        - **Retroceso Norteamérica**: De 0.8% (2015) a 0.2% (2024) por sanciones
        """)
    
    with tab2:
        st.subheader("Evolución Temporal por Región")
        
        # Selector de región
        region_seleccionada = st.selectbox(
            "Seleccione Región:",
            df_geo['Región'].tolist()
        )
        
        # Datos de la región seleccionada
        idx_region = df_geo[df_geo['Región'] == region_seleccionada].index[0]
        valores_region = df_geo.iloc[idx_region][['2010', '2015', '2020', '2024', '2026 Target']].values
        
        fig_region = go.Figure()
        
        fig_region.add_trace(go.Scatter(
            x=['2010', '2015', '2020', '2024', '2026 Target'],
            y=valores_region,
            mode='lines+markers',
            line=dict(color=colores_regiones[idx_region], width=4),
            marker=dict(size=15),
            fill='tozeroy',
            hovertemplate=f'{region_seleccionada}<br>Año: %{{x}}<br>% Ingresos: %{{y}}%<extra></extra>'
        ))
        
        fig_region.update_layout(
            title=f"Trayectoria de Ingresos: {region_seleccionada} (2010-2026)",
            xaxis_title="Período",
            yaxis_title="% de Ingresos Totales",
            height=400
        )
        
        st.plotly_chart(fig_region, use_container_width=True)
        
        # Cálculo de CAGR
        valor_2010 = valores_region[0]
        valor_2024 = valores_region[3]
        años_transcurridos = 14
        
        if valor_2010 > 0:
            cagr = ((valor_2024 / valor_2010) ** (1/años_transcurridos) - 1) * 100
        else:
            cagr = 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Valor 2010", f"{valor_2010:.1f}%", "")
        with col2:
            st.metric("Valor 2024", f"{valor_2024:.1f}%", f"{valor_2024 - valor_2010:+.1f} pp")
        with col3:
            st.metric("CAGR 2010-2024", f"{cagr:+.1f}%/año", "")
    
    with tab3:
        st.subheader("Fases de la Estrategia de Penetración")
        
        fases = [
            {
                'fase': 'Fase 1: Dominio China Rural',
                'periodo': '1997-2005',
                'estrategia': 'Periferia doméstica como campo de prueba',
                'logros': ['Desarrollo de soluciones personalizadas para condiciones adversas', 
                          'Construcción de base de clientes leales', 
                          'Validación tecnológica en ambientes menos exigentes']
            },
            {
                'fase': 'Fase 2: Penetración Emergentes',
                'periodo': '2006-2012',
                'estrategia': 'Exportar modelo exitoso a mercados similares',
                'logros': ['Entrada a Rusia (1997), África (2003), Latinoamérica (2002)',
                          'Alianzas con gobiernos y operadores locales',
                          'Modelo de "Value for Money" + Servicio 24/7']
            },
            {
                'fase': 'Fase 3: Asalto a Desarrollados',
                'periodo': '2013-2019',
                'estrategia': 'Competir frontalmente en Europa y Asia desarrollada',
                'logros': ['Contratos 5G con Vodafone, Telfort, operadores europeos',
                          'Superación de certificaciones estrictas',
                          'Reconocimiento como líder tecnológico (no solo precio)']
            },
            {
                'fase': 'Fase 4: Consolidación Post-Sanciones',
                'periodo': '2020-presente',
                'estrategia': 'Pivote hacia Global South y autonomía tecnológica',
                'logros': ['Fortalecimiento en África, Latam, Middle East, SEA',
                          'Desarrollo de HarmonyOS y HMS (independencia de Google)',
                          'Inversión masiva en semiconductores domésticos']
            }
        ]
        
        # Timeline visual
        fig_timeline = go.Figure()
        
        for i, fase_data in enumerate(fases):
            fig_timeline.add_trace(go.Scatter(
                x=[i],
                y=[1],
                mode='markers+text',
                name=fase_data['fase'],
                marker=dict(size=50, color=colores_regiones[i]),
                text=fase_data['periodo'],
                textposition='top center',
                textfont=dict(size=14, color='black'),
                hovertemplate=f"<b>{fase_data['fase']}</b><br>{fase_data['periodo']}<br>{fase_data['estrategia']}<extra></extra>"
            ))
        
        fig_timeline.update_layout(
            title="Timeline: Las 4 Fases de Penetración de Mercado de Huawei",
            xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
            yaxis=dict(showticklabels=False, showgrid=False, zeroline=False, range=[0.5, 1.5]),
            height=300,
            showlegend=False
        )
        
        st.plotly_chart(fig_timeline, use_container_width=True)
        
        # Expandibles con detalles de cada fase
        for fase_data in fases:
            with st.expander(f"📖 {fase_data['fase']} ({fase_data['periodo']})"):
                st.markdown(f"**Estrategia**: {fase_data['estrategia']}")
                st.markdown("**Logros Principales**:")
                for logro in fase_data['logros']:
                    st.markdown(f"- {logro}")
        
        st.success("""
        **🎯 Lección Estratégica Clave**:  
        
        La estrategia de "Periferia → Centro" de Huawei es un masterclass de Alineamiento Dinámico:
        
        1. **Empezar donde puedas ganar**: China rural tenía bajas barreras de entrada
        2. **Aprender haciendo**: Validar tecnología en ambientes reales antes de competir en ligas mayores
        3. **Construir reputación gradualmente**: De "barato" a "value for money" a "innovador"
        4. **Adaptar sin perder identidad**: Mantener core (customer-centricity, I+D) mientras se ajusta la propuesta
        5. **Pivotar ante crisis**: Sanciones USA → fortalecimiento en Global South + autonomía tecnológica
        
        **Resultado**: De $5,462 USD de capital inicial (1987) a $162B de ingresos proyectados (2026)
        """)

# ==================== ANÁLISIS DE RIESGOS ====================

elif vista_seleccionada == "⚠️ Análisis de Riesgos":
    st.header("⚠️ Análisis de Riesgos Estratégicos")
    st.markdown("### Identificación y Mitigación de Amenazas al Alineamiento Dinámico")
    
    df_riesgos = generar_datos_riesgos()
    
    # Métricas generales
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Riesgos Críticos", "2", "🔴 Alta Prioridad")
    with col2:
        st.metric("Riesgos Medios", "2", "🟡 Monitoreo")
    with col3:
        st.metric("Riesgos Bajos", "1", "🟢 Controlado")
    with col4:
        st.metric("Score Promedio", "6.3 / 10", "Nivel Medio-Alto")
    
    st.markdown("---")
    
    # Bubble chart (Probabilidad vs. Impacto)
    st.subheader("📊 Matriz de Riesgos: Probabilidad × Impacto")
    
    fig_riesgos = go.Figure()
    
    colors_riesgo = ['#FF4444', '#FFD700', '#00CC66', '#FFD700', '#FFD700']
    
    fig_riesgos.add_trace(go.Scatter(
        x=df_riesgos['Probabilidad'],
        y=df_riesgos['Impacto'],
        mode='markers+text',
        marker=dict(
            size=df_riesgos['Score'] * 10,
            color=colors_riesgo,
            line=dict(width=2, color='white')
        ),
        text=df_riesgos['Riesgo'],
        textposition='top center',
        textfont=dict(size=10, color='black'),
        hovertemplate='<b>%{text}</b><br>Probabilidad: %{x}%<br>Impacto: %{y}%<br>Score: ' + 
                      df_riesgos['Score'].astype(str) + '<extra></extra>'
    ))
    
    # Añadir cuadrantes
    fig_riesgos.add_shape(type="rect", x0=0, y0=0, x1=50, y1=50, 
                         fillcolor="lightgreen", opacity=0.2, line_width=0)
    fig_riesgos.add_shape(type="rect", x0=50, y0=0, x1=100, y1=50, 
                         fillcolor="yellow", opacity=0.2, line_width=0)
    fig_riesgos.add_shape(type="rect", x0=0, y0=50, x1=50, y1=100, 
                         fillcolor="orange", opacity=0.2, line_width=0)
    fig_riesgos.add_shape(type="rect", x0=50, y0=50, x1=100, y1=100, 
                         fillcolor="red", opacity=0.2, line_width=0)
    
    fig_riesgos.update_layout(
        title="Matriz de Riesgos (Tamaño del círculo = Urgencia de respuesta)",
        xaxis_title="Probabilidad (%)",
        yaxis_title="Impacto (%)",
        height=600,
        xaxis=dict(range=[0, 100]),
        yaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig_riesgos, use_container_width=True)
    
    st.markdown("---")
    
    # Tabla detallada de riesgos con estrategias de mitigación
    st.subheader("📋 Detalle de Riesgos y Estrategias de Mitigación")
    
    riesgos_detalle = [
        {
            'riesgo': 'Escalada tensión USA-China',
            'estado': '🔴',
            'score': 9.0,
            'probabilidad': '75%',
            'impacto': 'Crítico',
            'mitigacion': [
                'Diversificación geográfica acelerada (Global South)',
                'Autonomía tecnológica (semiconductores, OS, cloud)',
                'Lobby diplomático multilateral',
                'Construcción de supply chains alternativos'
            ],
            'kpi': 'Reducir dependencia de componentes USA/Taiwan de 60% a <20% para 2027'
        },
        {
            'riesgo': 'Fragmentación estándares 5G/6G',
            'estado': '🟡',
            'score': 6.5,
            'probabilidad': '50%',
            'impacto': 'Alto',
            'mitigacion': [
                'Liderazgo activo en 3GPP, ITU, y otros consorcios',
                'Alianzas estratégicas con Ericsson, Nokia en áreas no-competitivas',
                'Contribución masiva a estándares abiertos',
                'Posicionamiento como "puente" entre bloques geopolíticos'
            ],
            'kpi': 'Mantener >30% de patentes esenciales en estándares 6G'
        },
        {
            'riesgo': 'Obsolescencia modelos de negocio',
            'estado': '🟢',
            'score': 3.8,
            'probabilidad': '25%',
            'impacto': 'Medio',
            'mitigacion': [
                'Inversión continua en R&D (18.5% target 2026)',
                'Laboratorios de innovación en hubs globales',
                'Programa de corporate venture capital ($500M/año)',
                'Monitoreo de startups disruptivas (radar de señales débiles)'
            ],
            'kpi': '40% de ingresos provenientes de productos/servicios <3 años'
        },
        {
            'riesgo': 'Pérdida talento clave',
            'estado': '🟡',
            'score': 5.2,
            'probabilidad': '40%',
            'impacto': 'Alto',
            'mitigacion': [
                'Programas de retención (equity, bonus diferido)',
                'Cultura de innovación y autonomía (bottom-up)',
                'Plan de sucesión para roles críticos',
                'Employee branding internacional'
            ],
            'kpi': 'Retención de top talent >90%, diversidad en management 35%'
        },
        {
            'riesgo': 'Disrupción tecnológica (quantum, AI AGI)',
            'estado': '🟡',
            'score': 7.2,
            'probabilidad': '45%',
            'impacto': 'Crítico',
            'mitigacion': [
                'Apuestas tempranas en quantum computing y fotónica',
                'Alianzas con universidades de élite en IA avanzada',
                'Adquisiciones estratégicas de startups en frontier tech',
                'Modelo de "ambidexteridad" (exploit core + explore new)'
            ],
            'kpi': '15% de presupuesto R&D dedicado a tecnologías de horizonte 3'
        }
    ]
    
    for item in riesgos_detalle:
        with st.expander(f"{item['estado']} {item['riesgo']} (Score: {item['score']})"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Probabilidad**: {item['probabilidad']}")
                st.markdown(f"**Impacto**: {item['impacto']}")
            with col2:
                st.markdown(f"**Score de Riesgo**: {item['score']} / 10")
                st.markdown(f"**Estado**: {item['estado']}")
            
            st.markdown("**Estrategias de Mitigación**:")
            for estrategia in item['mitigacion']:
                st.markdown(f"- {estrategia}")
            
            st.info(f"**KPI de Monitoreo**: {item['kpi']}")
    
    st.markdown("---")
    
    # Recomendaciones para la Junta
    st.subheader("📌 Recomendaciones Urgentes para la Junta Directiva")
    
    recomendaciones = [
        {
            'titulo': '1. Intensificar Pivote hacia Ecosistemas de IA',
            'accion': 'Crear "Huawei AI Cloud Services" como BU independiente',
            'inversion': '$2B inicial',
            'metrica': 'Alcanzar 5% de ingresos desde AI-as-a-Service para 2026',
            'plazo': 'Q1 2025'
        },
        {
            'titulo': '2. Blindar Cadena de Suministro de Semiconductores',
            'accion': 'Acelerar inversión en SMIC y fabs domésticas',
            'inversion': '$5B adicionales',
            'metrica': '80% de chips en nodos <7nm producidos en China para 2027',
            'plazo': 'Q2 2025'
        },
        {
            'titulo': '3. Fortalecer Narrativa de Marca en Occidente',
            'accion': 'Campaña "Huawei para la Humanidad" (conectividad rural, telemedicina, educación)',
            'inversion': '$500M durante 2 años',
            'metrica': 'Aumentar Brand Perception en Europa/USA de 66 → 75 para 2026',
            'plazo': 'Q1 2025'
        },
        {
            'titulo': '4. Institucionalizar "Alineamiento Dinámico" como Capability',
            'accion': 'Crear "Office of Strategic Agility" reportando directo al CEO Rotativo',
            'inversion': '$50M/año (equipo + tecnología)',
            'metrica': 'Reducir tiempo detección → decisión de amenazas de 60 días a 15 días',
            'plazo': 'Q1 2025'
        }
    ]
    
    for rec in recomendaciones:
        st.markdown(f"### {rec['titulo']}")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Acción**: {rec['accion']}")
            st.markdown(f"**Inversión**: {rec['inversion']}")
        with col2:
            st.markdown(f"**Métrica de Éxito**: {rec['metrica']}")
            st.markdown(f"**Plazo de Implementación**: {rec['plazo']}")
        st.markdown("---")
    
    # Footer con advertencia
    st.error("""
    ⚠️ **ADVERTENCIA CRÍTICA**:  
    
    El riesgo geopolítico (Escalada USA-China, Score 9.0) representa una amenaza existencial para Huawei. 
    La Junta debe tratar este tema con **máxima prioridad** en cada sesión trimestral.
    
    **Sin mitigación efectiva**, Huawei podría perder acceso a:
    - Semiconductores avanzados (<7nm)
    - Mercados desarrollados (USA, UK, Australia, potencialmente más países europeos)
    - Cadenas de suministro críticas (TSMC, ASML, ARM)
    - Talento internacional (restricciones de visado)
    
    **Recomendación**: Crear un "War Room" permanente para gestión de crisis geopolítica.
    """)

# ==================== FOOTER ====================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666666; padding: 20px;'>
    <p><strong>Dashboard Ejecutivo: Alineamiento Dinámico - Caso Huawei</strong></p>
    <p>Desarrollado para INCAE Business School | Basado en el marco de Evolución Digital del Dr. Juan Carlos Barahona</p>
    <p>📊 Datos Simulados con Fines Académicos | 🔄 Última Actualización: Febrero 2026</p>
    <p style='font-size: 12px; margin-top: 10px;'>
        <em>"La transformación no es un destino tecnológico, sino un flujo ininterrumpido de conversaciones 
        y reconfiguraciones de comportamiento organizacional"</em> - Dr. Juan Carlos Barahona
    </p>
</div>
""", unsafe_allow_html=True)
