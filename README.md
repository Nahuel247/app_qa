# 📄🔎 Asistente de Preguntas sobre PDFs en Español

Este proyecto es una app interactiva construida con Streamlit que permite **subir un archivo PDF en español, hacer preguntas en lenguaje natural sobre su contenido y obtener respuestas automáticas** gracias a un modelo de lenguaje especializado en preguntas y respuestas.

## 🚀 Funcionalidades principales

✅ Carga de archivos PDF con extracción de texto.  
✅ Interfaz intuitiva con Streamlit para preguntas en español.  
✅ Respuestas inmediatas generadas por un modelo de QA entrenado en español.  
✅ Panel para visualizar el texto del PDF y las respuestas.  
✅ Compatible para ejecutarse localmente o desplegarse en la nube (Streamlit Cloud).

---

## 🔎 Modelo de lenguaje utilizado

El modelo utilizado es [PlanTL-GOB-ES/roberta-base-bne-sqac](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne-sqac), un modelo basado en RoBERTa entrenado para tareas de preguntas y respuestas extractivas en español.

---

## 🛠 Librerías utilizadas

- [Streamlit](https://streamlit.io/) – Para el desarrollo del dashboard interactivo.
- [PyPDF2](https://pypi.org/project/PyPDF2/) – Para leer y extraer texto de archivos PDF.
- [Transformers](https://huggingface.co/transformers/) – Para usar el modelo de lenguaje.
- [Torch](https://pytorch.org/) – Backend para el modelo de Transformers.

---

## 📦 Instalación local

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
