"""
App DataExtractorCV.
"""
#módulos:
import tempfile
import pandas as pd
import streamlit as st
from typing import Optional 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.document_loaders import PyPDFLoader

#Clase que describe la información que se desea extraer:
class Person(BaseModel):
    """Información sobre la persona:"""

    # ^ Doc-string para la entidad Person.
    # Este doc-string es enviado al LLM como una descripción del esquema de Person,
    # y puede ayudar a mejorar los resultados de la extracción.

    # Nota:
    # 1. Cada campo es `optional`.
    # 2. Cada campo tiene una `description` -- esta descripción es utilizada por el LLM.
    # Tener una buena descripción puede ayudar a mejorar los resultados de la extracción.
    Nombre: Optional[str]=Field(
        default=None, description="Nombres de la persona"
    )
    Apellido: Optional[str]=Field(
        default=None, description="Apellidos de la persona"
    )
    Profesion: Optional[str]=Field(
        default=None, description="Profesión de la persona"
    )
    Habilidades: Optional[str]=Field(
        default=None, description="Habilidades técnicas o no que tenga la persona, ejemplo:" \
        "lenguajes de programación, herramientas de software o de hardware, habilidades blandas, etc."
    )
    Idiomas: Optional[str]=Field(
        default=None, description="Idiomas que habla la persona y su nivel si se especifica."
    )

#prompt:
prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Eres un experto en algoritmos de extracción. "
            "Solo extrae información relevante. "
            "Si no conoce el valor de un atributo que se le pidió extraer,"
            "retorne null para el valor del atributo.",
        ),
        (
            "human", "{text}",
        )
    ]
)
#streamlit UI:
st.markdown(
    """
    <div style='text-align: center; padding: 20px; background-color: #17a589; border-radius: 10px; color: white;'>
        <div style='display: flex; justify-content: center; align-items: center; gap: 15px;'>
            <img src="https://cdn-icons-png.flaticon.com/128/3135/3135731.png" width="50">
            <h2 style="margin: 0;">Bienvenido al DataExtractorCV</h2>
        </div>
        <div style="display: flex; justify-content: center; gap: 40px; margin-top: 20px;">
            <a href="https://github.com/Brunoide7" target="_blank" style="text-decoration:none; color: white; display:flex; align-items:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" style="margin-right:8px;">
                Mas aplicaciones en GitHub
            </a>
            <a href="https://www.linkedin.com/in/bruno-ignacio-tolaba/" target="_blank" style="text-decoration:none; color: white; display:flex; align-items:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" style="margin-right:8px;">
                Contacto personal en LinkedIn
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

#configuración del llm:
def load_llm(openai_api_key):
    return ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

#ingreso de API Key:
openai_api_key = st.text_input("OpenAI API Key", type="password", placeholder="Ex: sk-2twmA8tfCb8un4...")

# Subir archivo PDF:
uploaded_file = st.file_uploader("Cargar archivo pdf..", type="pdf")

if uploaded_file is not None:
    #verificación de la api_key:
    if not openai_api_key:
        st.warning("Por favor inserte una API Key válida.")
        st.stop()
    
    #carga del modelo:
    llm = load_llm(openai_api_key)

    #guardar temporalmente el archivo para usarlo con PyPDFLoader:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    #usar PyPDFLoader con la ruta temporal:
    loader = PyPDFLoader(tmp_file_path)
    docs = loader.load()

    #cadena con estructura de salida definida por la clase Person:
    chain = prompt | llm.with_structured_output(schema=Person)

    #Extracción de datos:
    full_text = "\n".join([doc.page_content for doc in docs])
    respuesta = chain.invoke({"text": full_text})

    #Muestra de datos: 
    st.subheader("Informacion extraida:")
    df = pd.DataFrame(vars(respuesta), index=["Valores extraidos"]).T
    st.dataframe(df.rename(columns={"Valores extraidos": "Valor"}))