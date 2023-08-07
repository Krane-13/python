import os
from tkinter import filedialog
from zipfile import ZipFile, ZIP_DEFLATED

def compactar_tudo(diretorio):
    nomesarquivos = os.listdir()

    for nome in nomesarquivos:
        semextensao =nome.split('.')[0]
        nomezip=os.path.join(diretorio, semextensao + '.zip')
        arquivozip = ZipFile(nomezip, "w", compression=ZIP_DEFLATED)
        arquivozip.write(os.path.join(diretorio, nome), nome)
        arquivozip.close()
    return len(nomesarquivos)

if __name__ == '__main__':
    pasta = filedialog.askdirectory()
    print(f"Compactando arquivos em {pasta}")
    n = compactar_tudo(pasta)
    print(f"{n} arquivos compactadops com sucesso")
