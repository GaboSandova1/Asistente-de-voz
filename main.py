from streamlit_mic_recorder import speech_to_text
from gtts import gTTS
import streamlit as st
import requests
import json
import tempfile
import pygame
import time
import os

st.title("Asistente de voz con Ollama y Google TTS")

# Función para preguntar a Ollama
def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "model": "llama3",
                "prompt": f"Responde de forma concisa en español: {prompt}",
                "stream": False,
                "options": {"temperature": 0.1} 
            }),
            timeout=60
        )
        return response.json().get("response", "Error: Formato de respuesta inesperado")
    except requests.exceptions.RequestException as e:
        return f"Error de conexión: {str(e)}"
    except Exception as e:
        return f"Error inesperado: {str(e)}"

# Función para leer respuesta en voz alta con gTTS
def leer_con_gtts(texto):
    tts = gTTS(text=texto, lang='es', slow=False)
    # Crear la carpeta "Audios" si no existe
    os.makedirs("Audios", exist_ok=True)

    # Contar los archivos existentes en la carpeta "Audios"
    num_archivos = len([nombre for nombre in os.listdir("Audios") if nombre.startswith("respuesta") and nombre.endswith(".mp3")])

    ruta_mp3 = f"Audios/respuesta {num_archivos + 1}.mp3"
    tts.save(ruta_mp3)
    
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_mp3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)


# Captura de voz
texto = speech_to_text(language='es', start_prompt="🎤 Hablar", stop_prompt="⏹️ Detener", key='stt')

if texto:
    st.write("**Tú:**", texto)
    with st.spinner("Procesando..."):
        respuesta = ask_ollama(texto)
        st.write("**Asistente:**", respuesta)

    if st.button("Leer respuesta en voz alta"):
        leer_con_gtts(respuesta)
