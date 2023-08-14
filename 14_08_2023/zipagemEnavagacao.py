import os
from tkinter import filedialog
from zipfile import ZipFile, ZIP_DEFLATED

def compactar_tudo(diretorio):
    nomesarquivos = os.listdir(diretorio)
    nomedoarquivo = filedialog.asksaveasfile(mode='w')

    
    arquivozip = ZipFile(str(nomedoarquivo), "w", compression=ZIP_DEFLATED)
    for nome in nomesarquivos:
        
        arquivozip.write(os.path.join(diretorio, nome), nome)
    return len(nomesarquivos)
    arquivozip.close()
if __name__ == '__main__':
    pasta = filedialog.askdirectory()
    print(f"Compactando arquivos em {pasta}")
    n = compactar_tudo(pasta)
    print(f"{n} arquivos compactadops com sucesso")
