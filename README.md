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
- Interfaz desarrollada con Streamlit.
- Carga de archivos PDF para análisis.
- Extracción estructurada de información usando esquemas definidos con Pydantic.
- Integración con OpenAI y LangChain para procesamiento y extracción inteligente.
- Guarda temporalmente el PDF para su procesamiento con PyPDFLoader.
- Muestra los datos extraídos en una tabla interactiva.

## 📸 Captura / Demo

![Captura de pantalla](https://github.com/user-attachments/assets/6192d51c-f807-4ba6-8daf-ef953f9beb84)

## 📦 Requisitos / Instalación

```bash
git clone https://github.com/Brunoide7/DataExtractorCV.git
cd DataExtractorCV
pip install -r requirements.txt
streamlit run main.py
