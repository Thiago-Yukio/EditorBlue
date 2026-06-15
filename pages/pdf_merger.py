#Importando bibliotecas
import streamlit as st

#Importando as funções
from funcionalidades_pdf import obter_pdfs, juntar_pdfs



#Título da pagina
st.title('Mesclador de PDF')

#Campo para selecionar o nome do arquivo
nome_arquivo=st.text_input(
    label='arquivo',
    placeholder='Digite o nome do arquivo'
)

# Upload dos arquivos
# #Vizualização de arquivos baixados

upload =st.file_uploader(
    label='Escolha os arquivos em PDF',
    type='pdf',
    accept_multiple_files=True
)


colunas=st.columns(5)

with colunas[2]:
    botao=st.button('Juntar')
    if botao:
        #Carregar PDFs
        pdfs=obter_pdfs(upload)
        #Mesclando os PDFs
        pdf_unico=juntar_pdfs(pdfs)
        #Baixando o PDF
        st.download_button(
            label='Dowloand',
            data=pdf_unico,
            file_name=f'{nome_arquivo}.pdf',
            mime='application/octet-stream'
        )
