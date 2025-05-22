# 🧠 DataExtractorCV

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-blue?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pydantic-009688?style=for-the-badge&logo=pydantic&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
</p>

## 🔍 Extracción automática de datos de CVs en PDF

DataExtractorCV es una aplicación que extrae automáticamente información clave (nombre, apellido, profesión, habilidades e idiomas) de currículums en formato PDF utilizando un modelo de lenguaje de OpenAI a través de LangChain y Streamlit.

## ✨ Características principales
- Interfaz web desarrollada con Streamlit.
- Carga de archivos PDF para análisis.
- Extracción estructurada de información usando esquemas definidos con Pydantic.
- Integración con OpenAI y LangChain para procesamiento y extracción inteligente.
- Guarda temporalmente el PDF para su procesamiento con PyPDFLoader.
- Muestra los datos extraídos en una tabla interactiva.
- Compatible con despliegue en Streamlit Cloud.

## 📸 Captura / Demo

![Captura de pantalla](https://github.com/user-attachments/assets/6192d51c-f807-4ba6-8daf-ef953f9beb84)

👉 [Ver en Streamlit](https://appdataextractorcv.streamlit.app/)

## 📦 Requisitos / Instalación

```bash
git clone https://github.com/Brunoide7/DataExtractorCV.git
cd DataExtractorCV
pip install -r requirements.txt
streamlit run main.py
```
## 🛠️ Posibles mejoras

  - Añadir extracción de más campos como experiencia laboral, educación o certificaciones.

  - Incorporar soporte para múltiples idiomas en los documentos.
  
  - Soporte para procesar múltiples PDFs a la vez.

  - Mejora de la precisión usando técnicas de RAG (Retrieval-Augmented Generation) con contexto adicional.

  - Almacenamiento opcional en bases de datos como SQLite o Firebase.

## 🧩 Posibles variantes de extractor
La misma lógica de extracción puede adaptarse fácilmente a otras aplicaciones como:

- Extractor de noticias: toma URLs o textos completos de noticias y extrae título, fecha, autor, y resumen.
  
- Extractor de contratos: identifica nombres de partes involucradas, fechas clave, cláusulas importantes, etc.
  
- Extractor de facturas: detecta número de factura, fecha, cliente, monto total, productos listados.
  
- Extractor de papers académicos: obtiene título, autores, resumen, palabras clave y referencias.
