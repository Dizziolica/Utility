import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Qual o diretorio")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"], }

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            os.mkdir(f"{caminho}/{pasta}")
        os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
