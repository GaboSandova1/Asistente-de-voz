from streamlit_mic_recorder import speech_to_text
import streamlit as st
import requests
import json
import pyttsx3

# Configuración
st.title("Asistente de voz con Ollama ")

# Función para leer en voz alta
def leer_texto(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # velocidad
    engine.setProperty('voice', 'spanish')  # intentar usar una voz en español si está disponible
    engine.say(texto)
    engine.runAndWait()

# Función para consultar a Ollama
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

# Captura de voz
texto = speech_to_text(
    language='es',
    start_prompt="🎤 Hablar",
    stop_prompt="⏹️ Detener",
    key='stt'
)

# Procesamiento
if texto:
    st.write("**Tú:**", texto)
    with st.spinner("Procesando..."):
        respuesta = ask_ollama(texto)
        st.write("**Asistente:**", respuesta)

        # Botón para leer la respuesta
        if st.button("🔊 Leer respuesta"):
            leer_texto(respuesta)
