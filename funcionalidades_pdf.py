from pypdf import PdfReader,PdfWriter

def obter_pdfs(arquivos: list) ->list:
    """
    Função que têm como objetivo buscar e obter os arquivos em extensão .PDF
    :param arquivos: arquivo PDFs
    :return: Lista de arquivos PDFs
    """

    #Lista com os arquivos PDFs
    lista_pdfs=[]

    #Carregar os arquivos
    for arquivo in arquivos:
        #Carregar o arquivo
        pdf_load=PdfReader(arquivo)
        lista_pdfs.append(pdf_load)

    return lista_pdfs


def juntar_pdfs(pdfs: list) ->object:
    """
    Função respinsavel em juntar os PDFs
    :param pdfs: Lista com os PDFs separados
    :return: Arquivo unico PDF
    """

    merger=PdfWriter()

    #Adicionando os arquivos ao merger
    for pdf in pdfs:
        merger.append(pdf)

    #escrever o arquivo PDF unico
    merger.write('arquivo_temp.pdf')
    merger.close()

    #ler de bytes para arquivo legivel
    with open('arquivo_temp.pdf','rb') as arquivo:
        arquivo_legivel=arquivo.read()

    return arquivo_legivel