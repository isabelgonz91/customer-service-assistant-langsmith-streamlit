# app.py
import streamlit as st
from langsmith_integration import LangSmithLLM
import toml

# Cargar las claves API desde secrets.toml
secrets = toml.load("secrets.toml")
openai_api_key = secrets.get("OPENAI_API_KEY")
langsmith_api_key = secrets.get("LANGSMITH_API_KEY")

if not openai_api_key or not langsmith_api_key:
    st.error("Claves API no encontradas. Por favor, añade tus claves API en secrets.toml.")
else:
    llm = LangSmithLLM(openai_api_key, langsmith_api_key)

    # Título de la aplicación
    st.title("Asistente de Atención al Cliente")

    # Selección del tipo de consulta
    option = st.selectbox(
        "Seleccione el tipo de consulta:",
        ("Pregunta Frecuente", "Información del Producto")
    )

    if option == "Pregunta Frecuente":
        faq_question = st.text_input("Escribe tu pregunta:")
        if st.button("Obtener Respuesta"):
            if faq_question:
                response = llm.handle_faq(faq_question)
                st.write("Respuesta del Modelo:")
                st.write(response)
            else:
                st.write("Por favor, escribe una pregunta.")

    elif option == "Información del Producto":
        product_name = st.text_input("Escribe el nombre del producto:")
        if st.button("Obtener Información"):
            if product_name:
                response = llm.generate_product_info(product_name)
                st.write("Información del Producto:")
                st.write(response)
            else:
                st.write("Por favor, escribe el nombre de un producto.")

    # Información adicional
    st.sidebar.title("Sobre esta aplicación")
    st.sidebar.info(
        """
        Esta aplicación utiliza LangSmith para proporcionar información sobre productos y responder preguntas frecuentes de los clientes.
        """
    )
