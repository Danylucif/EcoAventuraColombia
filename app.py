import streamlit as st
import pandas as pd
import base64
import os
from streamlit_folium import st_folium

# Importaciones modulares limpias y corregidas
from modules.mapas import crear_mapa_biodiversidad
from modules.juegos import iniciar_trivia
from modules.calculadora import calcular_huella_co2, calcular_consumo_agua, calcular_arboles_compensacion
from modules.descargas import generar_pdf_certificado
from modules.reportes import guardar_reporte_fauna, cargar_todos_los_reportes
from modules.fauna import mostrar_catalogo_fauna

# Configuración avanzada de la página web
st.set_page_config(page_title="EcoAventuraColombia", layout="wide", initial_sidebar_state="expanded")

def poner_fondo_pantalla(ruta_imagen):
    try:
        with open(ruta_imagen, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded_string}");
                background-size: cover; background-position: center; background-attachment: fixed;
            }}
            h1, h2, h3, p, span, label, .stMarkdown {{
                color: #FFFFFF !important;
                text-shadow: 2px 2px 8px #000000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000 !important;
            }}
            .stDataFrame {{ background-color: rgba(255, 255, 255, 0.9) !important; border-radius: 10px; padding: 10px; }}
            [data-testid="stSidebar"] {{ background-color: rgba(15, 30, 15, 0.9) !important; }}
            [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {{ color: #FFFFFF !important; text-shadow: none !important; }}
            </style>
            """, unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("⚠️ Archivo de fondo no encontrado.")

poner_fondo_pantalla("data/fondo.jpg")

def convertir_imagen_local(ruta):
    if os.path.exists(ruta):
        with open(ruta, "rb") as f:
            return f"data:image/jpg;base64,{base64.b64encode(f.read()).decode()}"
    return "https://unsplash.com"

st.title("🌿 EcoAventuraColombia")
st.caption("Plataforma Tecnológica Interactiva para la Exploración y Conservación Ambiental")

# Menú del panel de control
menu = st.sidebar.selectbox(
    "📊 MENÚ DE NAVEGACIÓN",
    ["Inicio", "Regiones de Colombia", "Mapa de Fauna Silvestres", "Fichas de Fauna Silvestre", "Flora de Colombia", "Juegos Educativos", "Audioteca de la Naturaleza", "Calculadora Ecológica", "Reportes de Alertas", "Monitoreo Hídrico"]
)

if menu == "Inicio":
    st.header("¡Bienvenidos a EcoAventuraColombia!")
    st.write("Explora la riqueza biológica de nuestro país, enfocándote en la fauna silvestre, la flora, los páramos y los recursos hídricos.")

elif menu == "Fichas de Fauna Silvestre":
    mostrar_catalogo_fauna()

elif menu == "Regiones de Colombia":
    st.header("📊 Datos de Biodiversidad por Región")
    datos_regiones = {
        "Región": ["Andina", "Amazonía", "Pacífico", "Caribe", "Orinoquía", "Insular"],
        "Ecosistema Clave": ["Páramos", "Selva Húmeda", "Manglares", "Bosque Seco", "Sabanas", "Arrecifes"],
        "Fauna Insigne": ["Cóndor", "Jaguar", "Rana Dorada", "Guacamaya", "Chigüiro", "Tortuga Carey"]
    }
    st.dataframe(pd.DataFrame(datos_regiones), use_container_width=True)

elif menu == "Mapa de Fauna Silvestre":
    st.header("🗺️ Mapa Geográfico de Fauna Silvestre")
    st.write("Haz clic sobre los marcadores geográficos para descubrir animales en sus hábitats.")
    st_folium(crear_mapa_biodiversidad(), width=1000, height=500)

elif menu == "Flora de Colombia":
    st.header("🌸 Catálogo de Flora Nacional e Insumos Forestales")
    buscar_planta = st.text_input("🔍 Buscar planta por nombre:", "").lower()
    
    plantas = [
        {"nombre": "Frailejón", "cientifico": "Espeletia", "img": convertir_imagen_local("data/frailejon.jpg"), "desc": "La verdadera 'fábrica de agua' de la alta montaña. Sus hojas capturan la neblina y la filtran hacia los ríos."},
        {"nombre": "Palma de Cera", "cientifico": "Ceroxylon quindiuense", "img": convertir_imagen_local("data/palma.jpg"), "desc": "Árbol nacional de Colombia y la palma más alta del mundo. Crece en los bosques andinos."},
        {"nombre": "Orquídea Cattleya", "cientifico": "Cattleya trianae", "img": convertir_imagen_local("data/orquidea.jpg"), "desc": "Flor nacional de Colombia. Es una planta epífita de los bosques andinos de increíble belleza."}
    ]
    
    plantas_filtradas = [p for p in plantas if buscar_planta in p["nombre"].lower()]
    if not plantas_filtradas:
        st.warning("⚠️ No se encontraron especies.")
    else:
        columnas = st.columns(len(plantas_filtradas))
        for idx, planta in enumerate(plantas_filtradas):
            with columnas[idx]:
                st.markdown(f"### {planta['nombre']}")
                st.markdown(f"*{planta['cientifico']}*")
                st.markdown(f'<img src="{planta["img"]}" style="width:100%; border-radius:8px; box-shadow: 2px 2px 5px rgba(0,0,0,0.4);">', unsafe_allow_html=True)
                st.write(planta["desc"])

elif menu == "Juegos Educativos":
    iniciar_trivia()

elif menu == "Audioteca de la Naturaleza":
    st.header("🎵 Paisajes Sonoros de Colombia")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🦅 Canto de Alta Montaña")
        if os.path.exists("data/ave.mp3"): st.audio("data/ave.mp3", format="audio/mp3")
    with col2:
        st.markdown("### 🐾 Rugido de la Selva")
        if os.path.exists("data/jaguar.mp3"): st.audio("data/jaguar.mp3", format="audio/mp3")
    with col3:
        st.markdown("### 🌧️ Viento en el Páramo")
        if os.path.exists("data/paramo.mp3"): st.audio("data/paramo.mp3", format="audio/mp3")

elif menu == "Calculadora Ecológica":
    st.header("🌲 Calculadora de Impacto Ambiental e Hidrológico")
    
    nombre_usuario = st.text_input("Ingresa tu nombre completo para el certificado:", "Ciudadano Ambiental")
    
    if 'calculado' not in st.session_state:
        st.session_state.calculado = False
        st.session_state.t_co2 = 0.0
        st.session_state.agua_m3 = 0.0
        st.session_state.arboles = 0
        st.session_state.tipo_arbol = ""
        st.session_state.nombre_cert = ""

    with st.form("calculadora_huella"):
        col1, col2 = st.columns(2)
        with col1:
            transporte = st.number_input("Kilómetros en vehículo a la semana:", min_value=0.0, value=20.0)
            energia = st.number_input("Consumo eléctrico mensual (kWh):", min_value=0.0, value=120.0)
        with col2:
            agua_mes = st.number_input("Consumo de agua mensual de tu hogar (M³ en tu recibo):", min_value=0.0, value=12.0)
            residuos = st.slider("Bolsas de basura no reciclada semanales:", min_value=1, max_value=10, value=2)
            
        tipo_arbol_input = st.selectbox("Especie nativa a apadrinar para mitigar:", ["Frailejón (Alta Montaña)", "Palma de Cera (Bosque Andino)", "Arboloco (Restauración Rápida)"])
        boton_calcular = st.form_submit_button("Calcular mi Impacto Ambiental")
        
        if boton_calcular:
            t_co2, kg_co2 = calcular_huella_co2(transporte, energia, residuos)
            agua_m3, agua_litros = calcular_consumo_agua(agua_mes)
            st.session_state.calculado = True
            st.session_state.t_co2 = t_co2
            st.session_state.agua_m3 = agua_m3
            st.session_state.agua_litros_str = f"{agua_litros:,}"
            st.session_state.arboles = calcular_arboles_compensacion(kg_co2, agua_m3, tipo_arbol_input)
            st.session_state.tipo_arbol = tipo_arbol_input
            st.session_state.nombre_cert = nombre_usuario

    if st.session_state.calculado:
        st.markdown("---")
        st.subheader("📊 Diagnóstico de Recursos de Ciencia Ciudadana")
        metricas_col1, metricas_col2 = st.columns(2)
        with metricas_col1:
            st.metric(label="💨 Tu Emisión Estimada de CO₂", value=f"{st.session_state.t_co2:.2f} Toneladas / año")
        with metricas_col2:
            st.metric(label="💧 Tu Consumo Estimado de Agua", value=f"{st.session_state.agua_m3:.0f} M³ / año", delta=f"{st.session_state.agua_litros_str} Litros")
        
        st.success(f"🌱 Para neutralizar tu huella de carbono y proteger los caudales hídricos, deberías sembrar y cuidar **{st.session_state.arboles}** ejemplares de **{st.session_state.tipo_arbol}** en las cuencas colombianas.")
        
        pdf_archivo = generar_pdf_certificado(
            st.session_state.nombre_cert, 
            st.session_state.t_co2, 
            st.session_state.agua_m3, 
            st.session_state.arboles, 
            st.session_state.tipo_arbol
        )
        st.download_button(
            label="📥 Descargar mi Certificado Ecológico en PDF",
            data=pdf_archivo,
            file_name="Certificado_Compensacion_EcoAventura.pdf",
            mime="application/pdf"
        )

elif menu == "Reporte de Alertas":
    st.header("🦅 Centro de Reportes de Fauna Silvestre")
    with st.form("formulario_fauna"):
        col1, col2 = st.columns(2)
        with col1:
            departamento = st.selectbox("Departamento:", ["Caldas", "Antioquia", "Cundinamarca", "Valle del Cauca", "Amazonas", "Meta"])
            grupo_animal = st.selectbox("Clase:", ["Mamífero", "Ave", "Reptil", "Anfibio"])
        with col2:
            estado = st.radio("Estado:", ["Sano", "Herido / En peligro", "Presunto Tráfico Ilegal"])
            detalles = st.text_area("Descripción:")
        enviado = st.form_submit_button("Radicar Reporte Ambiental")
        
        if enviado:
            # CORREGIDO: Se cambió 'group_animal' por la variable correcta 'grupo_animal'
            guardar_reporte_fauna(departamento, grupo_animal, estado, detalles)
            st.success("✅ Alerta registrada con éxito.")
            
    df_reportes = cargar_todos_los_reportes()







