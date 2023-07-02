# Crie um programa que tenta criar um arquivo novo e, caso detecte FileExistsError, renomeia o arquivo com um "_1" ao final.
import os
def renomear_arquivo(texto):
    try:
        with open('texto.txt', 'x'):
            print(f"arquivo '{texto}' criado com sucesso")
    except FileExistsError:
        novo = f"{texto}_1"
        print(f"O arquivo '{texto}' já existe. Renomeando para '{novo}'")
        renomear_arquivo(novo)


# Crie um programa que pede um nome de um arquivo para ser aberto, abre e imprime seu conteúdo na tela, mas desta vez usando um contexto.
def ler_arquivo(texto):
    try:
        with open("texto.", 'r') as file:
            conteudo = file.read()
            print(f"Conteúdo do arquivo '{texto}':")
            print(conteudo)
    except FileNotFoundError:
        print(f"O arquivo '{texto}' não foi encontrado.")
    except PermissionError:
        print(f"Sem permissão para abrir o arquivo '{texto}'.")
