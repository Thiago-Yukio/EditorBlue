#Importando bibliotecas
import streamlit as st

#Título da pagina
st.title('Visualizador JPEG')

#Campo para enviar o arquivo em jpeg

imagem_jpegs=st.file_uploader(
    label='Escolha um arquivo PNG',
    type='jpeg',
    accept_multiple_files=True
)

for imagem_jpeg in imagem_jpegs:
    if imagem_jpeg is not None:
        st.image(imagem_jpeg)