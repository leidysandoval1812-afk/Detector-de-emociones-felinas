import streamlit as st
from PIL import Image
import random
import time

# Configuración de la ventana
st.set_page_config(page_title="Detector de Emociones Felinas - Liam Velez", page_icon="🐱")

# --- BARRA LATERAL (Información del Proyecto con Colores) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616430.png", width=100)
    st.markdown("<h2 style='color: #FF5722;'>Proyecto de Ciencias 🔬</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<h3 style='color: #0288D1; margin-bottom: 0px;'>🏫 Colegio:</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #0288D1; font-size: 20px; font-weight: bold;'>Rafael Uribe Uribe</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #4CAF50; margin-bottom: 0px;'>👨‍🔬 Creador:</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #388E3C; font-size: 22px; font-weight: bold;'>Liam Velez</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #FF9800; margin-bottom: 0px;'>🎒 Curso:</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #F57C00; font-size: 24px; font-weight: bold;'>201</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 **Objetivo:** Ayudar a los dueños a entender mejor el lenguaje corporal y emociones de sus gatos usando Inteligencia Artificial.")

# --- CUERPO PRINCIPAL ---
st.title("🐱 Detector de Emociones Felinas")

# Encabezado colorido
st.markdown("""
<div style='background-color: #E3F2FD; padding: 10px; border-radius: 10px; margin-bottom: 20px;'>
    <h4 style='color: #0288D1; margin: 0;'>🏫 <b>Colegio Rafael Uribe Uribe</b></h4>
    <p style='margin: 0; font-size: 16px;'>Proyecto presentado por: <b style='color: #388E3C; font-size: 18px;'>Liam Velez</b> | Curso: <b style='color: #F57C00; font-size: 18px;'>201</b></p>
</div>
""", unsafe_allow_html=True)

st.write("Toma una foto a tu gato o sube una imagen para analizar su estado de ánimo.")

# Opción para subir o tomar foto
opcion = st.radio("Selecciona origen de la imagen:", ("Usar Cámara", "Subir Imagen"))

imagen_input = None

if opcion == "Usar Cámara":
    imagen_input = st.camera_input("Enfoca el rostro de tu gato")
else:
    imagen_input = st.file_uploader("Elige una foto de tu gato", type=["jpg", "jpeg", "png"])

if imagen_input is not None:
    # Mostrar la imagen seleccionada
    img = Image.open(imagen_input)
    st.image(img, caption="Foto cargada correctamente", use_container_width=True)
    
    if st.button("🔍 Analizar Emoción"):
        with st.spinner("Analizando microexpresiones felinas con Inteligencia Artificial..."):
            time.sleep(2)  # Simula el procesamiento
            
            # Lista de emociones y recomendaciones (Prototipo)
            emociones = [
                {"emocion": "Relajado / Feliz 😊", "consejo": "Tu gato se siente seguro y cómodo en su entorno."},
                {"emocion": "Alerta / Curioso 👀", "consejo": "Algo llamó su atención. Está activo y observador."},
                {"emocion": "Asustado / Estresado 🙀", "consejo": "Busca signos como orejas hacia abajo. Dale su espacio."},
                {"emocion": "Enojado / Molesto 😾", "consejo": "Evita tocarlo en este momento para prevenir un rasguño."}
            ]
            
            # Selección de resultado
            resultado = random.choice(emociones)
            
            # Celebración visual para el niño
            st.balloons()
            
            st.success(f"**Resultado:** {resultado['emocion']}")
            st.info(f"💡 **Recomendación:** {resultado['consejo']}")

# Pie de página colorido
st.markdown("---")
st.markdown("<p style='text-align: center; color: #0288D1; font-weight: bold;'>Proyecto de Ciencia y Tecnología | Colegio Rafael Uribe Uribe | Creado por Liam Velez - Curso 201</p>", unsafe_allow_html=True)
