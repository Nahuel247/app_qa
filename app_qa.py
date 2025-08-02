#####################################################
# APLICACIÓN PARA RESPONDER PREGUNTAS DE UN TEXTO
#####################################################
#  Autor: Nahuel Canelo
# Correo: nahuelcaneloaraya@gmail.com

###########################
# IMPORTAMOS LIBRERÍAS
###########################

import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline


##############################
# DEFINIMOS FUNCIONES
#############################


# Configura el pipeline QA en español
@st.cache_resource
def load_pipeline():
    return pipeline(
        task="question-answering",
        model="distilbert-base-cased-distilled-squad",
        #model="PlanTL-GOB-ES/roberta-base-bne-sqac",
        #model="google/flan-t5-large",
        #model="HuggingFaceH4/zephyr-7b-beta",
        #model="google/flan-t5-large"
        framework="pt"
    )


#################################
# EJECUTAMOS PROCESO
#################################


qa_pipeline = load_pipeline()

st.title("📄🔎 Asistente de Preguntas sobre PDFs en Español")

# Cargar archivo PDF
uploaded_file = st.file_uploader("Sube un archivo PDF para analizar:", type="pdf")

if uploaded_file is not None:
    # Extraer texto
    reader = PdfReader(uploaded_file)
    document_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            document_text += page_text + "\n"

    if document_text.strip():
        st.subheader("Texto extraído del PDF:")
        with st.expander("Mostrar/Ocultar texto"):
            st.write(document_text)

        # Área para hacer preguntas
        st.subheader("Escribe tu pregunta sobre el contenido del PDF:")
        question = st.text_input("Pregunta:", placeholder="¿Qué dice el documento sobre...?", key="pregunta")

        if question:
            # Ejecutar QA
            with st.spinner("Buscando respuesta..."):
                result = qa_pipeline({
                    "context": document_text,
                    "question": question
                })
            st.success("Respuesta encontrada:")
            st.write(f"**{result['answer']}** (confianza: {result['score']:.4f})")
    else:
        st.error("No se pudo extraer texto del PDF. Asegúrate de que el PDF contiene texto seleccionable (no solo imágenes).")
else:
    st.info("Por favor, sube un archivo PDF para comenzar.")




#streamlit run app_qa.py
