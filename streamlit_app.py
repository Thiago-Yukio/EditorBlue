#Bibliotecas usadas
import streamlit as st

#Configurações da página
st.set_page_config(
    page_title='EditorBlue',
    page_icon='🧊',
    layout='centered'
)

#Menu de navegação
pagina=st.navigation([
    st.Page('pages/pdf_merger.py', title=' Juntador PDF'),
    st.Page('pages/visualizador_pdf.py', title=' Visualizador PDF'),
    st.Page('pages/visualizador_png.py', title='visualizador PNG'),
    st.Page('pages/visualizador_jpeg.py', title='visualizador JPEG'),

])
pagina.run()