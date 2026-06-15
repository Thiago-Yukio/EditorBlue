#Importando bibliotecas
import streamlit as st

#Título da pagina
st.title('Visualizador de PDF')

#Campo para enviar o arquivo
uploads=st.file_uploader(
    label='Escolha um arquivo PDF',
    type='pdf',
    accept_multiple_files=True
)

#Mostrar o arquivo PDF no site
for upload in uploads:
    if upload is not None:
        st.pdf(upload)