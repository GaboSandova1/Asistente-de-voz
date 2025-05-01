from streamlit_mic_recorder import speech_to_text
import streamlit as st
import requests
import json

# Configuración
st.title("Asistente de voz con Ollama ")

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
            timeout=15
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