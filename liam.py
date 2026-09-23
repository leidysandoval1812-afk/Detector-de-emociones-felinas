import streamlit as st
from PIL import Image
import random
import time

# Configuración de la ventana
st.set_page_config(page_title="Cat Emotion Detector", page_icon="🐱")

st.title("🐱 Detector de Emociones Felinas")
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
    st.image(img, caption="Foto procesada", use_container_width=True)
    
    if st.button("Analizar Emoción"):
        with st.spinner("Analizando microexpresiones felinas..."):
            time.sleep(2)  # Simula el procesamiento
            
            # Lista de emociones y recomendaciones (Prototipo)
            emociones = [
                {"emocion": "Relajado / Feliz 😊", "consejo": "Tu gato se siente seguro y cómodo en su entorno."},
                {"emocion": "Alerta / Curioso 👀", "consejo": "Algo llamó su atención. Está activo y observador."},
                {"emocion": "Asustado / Estresado 🙀", "consejo": "Busca signos como orejas hacia abajo. Dale su espacio."},
                {"emocion": "Enojado / Molesto 😾", "consejo": "Evita tocarlo en este momento para prevenir un rasguño."}
            ]
            
            # Selección de resultado (Aquí se conectará el modelo de IA real)
            resultado = random.choice(emociones)
            
            st.success(f"**Resultado:** {resultado['emocion']}")
            st.info(f"💡 **Recomendación:** {resultado['consejo']}")
            