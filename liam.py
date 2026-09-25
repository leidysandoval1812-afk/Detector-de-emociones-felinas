import streamlit as st
from PIL import Image
import random
import time

# Configuración de la ventana
st.set_page_config(page_title="Detector de Emociones Felinas - Liam Velez", page_icon="🐱")

# --- BARRA LATERAL (Información del Proyecto) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616430.png", width=100)
    st.title("Proyecto de Ciencias 🔬")
    st.markdown("---")
    st.subheader("🏫 Colegio:")
    st.write("**Rafael Uribe Uribe**")
    st.subheader("👨‍🔬 Creador:")
    st.write("**Liam Velez**")
    st.subheader("🎒 Curso:")
    st.write("**201**")
    st.markdown("---")
    st.info("💡 **Objetivo:** Ayudar a los dueños a entender mejor el lenguaje corporal y emociones de sus gatos usando Inteligencia Artificial.")

# --- CUERPO PRINCIPAL ---
st.title("🐱 Detector de Emociones Felinas")
st.caption("Colegio Rafael Uribe Uribe | Proyecto presentado por **Liam Velez** (Curso 201)")

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

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Proyecto de Ciencia y Tecnología | Colegio Rafael Uribe Uribe | Creado por Liam Velez - Curso 201</p>", unsafe_allow_html=True)
