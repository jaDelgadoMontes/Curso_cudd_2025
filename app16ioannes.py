import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbot")

openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("Ingresa tu consulta")
if prompt==None:
   st.stop()

with st.chat_message("user", avatar = "🦖"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.
contexto = """
La asignatura es impartida por M.E. Juan Armando DelgadoMontes. 
Su teléfono es 614 2730080.
En la asigantura de Bioestadística se incriben estudiantes de tercer semestre de la Licenciatura en Nutrición. "
"""
promptFinal = contexto + prompt
stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": promptFinal}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content

with st.chat_message("assistant"):
   st.write(respuesta)
