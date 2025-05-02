## Asistente de voz con Ollama, Streamlit y gTTS:

Este proyecto es un asistente de voz local en español que permite interactuar por voz con un modelo LLM (Llama3) usando [Ollama](https://ollama.com), `streamlit` para la interfaz, y `gTTS` + `pygame` para convertir texto en voz.

## Características:

- Reconocimiento de voz desde el navegador con `streamlit_mic_recorder`.
- Comunicación con el modelo `llama3` local de Ollama.
- Lectura de respuestas en voz alta usando Google Text-to-Speech (`gTTS`).
- Interfaz simple y amigable con `Streamlit`.

## Requisitos:

- Python 3.9 o superior
- Ollama instalado y corriendo localmente
- Modelo `llama3` descargado en Ollama
- Paquetes de Python:

```bash
pip install streamlit streamlit-mic-recorder requests pygame gtts
```

## Instalacion y Ejecucion:

- Instala Ollama desde https://ollama.com
- Carga el modelo Llama3 en tu máquina:

```bash
ollama pull llama3
```

- Ejecuta el assistente de voz

```bash
streamlit run main.py #No lo corras desde el python, tiene que ser en la terminal de tu editor con este comando
```

## Uso:

- Presiona el botón de 🎤 para hablar.
- Espera a que se procese tu voz.
- El modelo generará una respuesta y podrás escucharla presionando el botón 🔊.

## Nota:

- La voz generada es proporcionada por Google Text-to-Speech y puede variar según idioma y sistema.
- El modelo LLM se ejecuta localmente, por lo que no requiere conexión a Internet para generar respuestas.
- Si tienes problemas con la voz o el micrófono, asegúrate de dar permisos al navegador y tener configurado correctamente el audio.












