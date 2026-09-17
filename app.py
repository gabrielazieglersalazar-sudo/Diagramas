import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Documentación de la Planta", page_icon="🏭", layout="wide")

# --- CABECERA Y LOGOS ---
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    try:
        st.image("logo_escuela.png", width=150)
    except FileNotFoundError:
        st.warning("Logo de escuela no encontrado")

with col2:
    st.markdown("<h1 style='text-align: center; color: #003366;'>Diagramas de la Planta</h1>", unsafe_allow_html=True)
    
    # Aquí agregamos los autores y tutores con una fuente diferente (Georgia) y tamaño ajustado
    st.markdown("""
        <p style='text-align: center; color: #333333; font-family: "Georgia", serif; font-size: 18px;'>
            <b>Realizado por:</b> E. Nicole Palencia, Marie Paternina y Gabriela Ziegler.<br>
            <b>Tutores:</b> Ing. Raúl Páez e Ing. Joan Giralt
        </p>
        """, unsafe_allow_html=True)

with col3:
    try:
        st.image("logo_empresa.png", width=150)
    except FileNotFoundError:
        st.warning("Logo de empresa no encontrado")

st.markdown("---")

# --- FUNCIÓN PARA MOSTRAR PDFs ---
def mostrar_pdf(ruta_archivo):
    try:
        # Usamos el nuevo componente seguro para renderizar PDFs
        pdf_viewer(ruta_archivo)
    except Exception:
        st.error(f"❌ Ocurrió un error al intentar mostrar el archivo: {ruta_archivo}")

# --- SECCIÓN 1: DBP ---
st.subheader("1. Diagramas de Bloques de Procesos (DBP)")
archivo_dbp = "Diagramas - Palencia,Paternina,Ziegler-DBP.drawio.pdf"

# Mostrar visor
mostrar_pdf(archivo_dbp)

# Botón de descarga
try:
    with open(archivo_dbp, "rb") as f:
        st.download_button(label="📥 Descargar DBP (Opcional)", data=f, file_name=archivo_dbp, mime="application/pdf", key="btn_dbp")
except FileNotFoundError:
    pass

st.markdown("---")

# --- SECCIÓN 2: Simbología ---
st.subheader("2. Hoja de Simbología")
archivo_simb = "HojaDeSimbologia.drawio.pdf"

mostrar_pdf(archivo_simb)

try:
    with open(archivo_simb, "rb") as f:
        st.download_button(label="📥 Descargar Simbología (Opcional)", data=f, file_name=archivo_simb, mime="application/pdf", key="btn_simb")
except FileNotFoundError:
    pass

st.markdown("---")

# --- SECCIÓN 3: DFP ---
st.subheader("3. Diagramas de Flujo de Procesos (DFP)")
archivo_dfp = "DFP FINAL.pdf"

mostrar_pdf(archivo_dfp)

try:
    with open(archivo_dfp, "rb") as f:
        st.download_button(label="📥 Descargar DFP Final (Opcional)", data=f, file_name=archivo_dfp, mime="application/pdf", key="btn_dfp")
except FileNotFoundError:
    pass