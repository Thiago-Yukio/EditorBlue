#Importando bibliotecas
import streamlit as st

#Título da pagina
st.title('Visualizador PNG')

#Campo para enviar o arquivo em pngs

imagens_pngs=st.file_uploader(
    label='Escolha um arquivo PNG',
    type='png',
    accept_multiple_files=True
)

for imagem_png in imagens_pngs:
    if imagem_png is not None:
        st.image(imagem_png)