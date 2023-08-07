import tkinter
import os

def selecionar_pasta(arg):
    subpasta = lista_dir.get(lista_dir.curselection())
    endereco = entrada.get()
    if not endereco[-1] == '/':
        endereco = endereco + '/'
    endereco = endereco + subpasta + '/'
    entrada.delete(0,tkinter.END)
    entrada.insert(0,endereco)
    clique_botao()
    

def clique_botao():
    lista_dir.delete(0, lista_dir.size())
    endereco = entrada.get()
    try:
        conteudo = os.listdir(endereco)
    except FileNotFoundError:
        lista_dir.insert(0, "Pasta nao encontrada")
    except NotADirectoryError:
        lista_dir.insert(0, "Nao e diretorio")
    else:
        for i in range(len(conteudo)):
            lista_dir.insert(i, conteudo[i])

def clique_voltar():
    endereco = entrada.get()
    if endereco == '/':
        print("diretorio raiz")
        return
    if endereco[-1] == '/':
        endereco =  endereco[:-1]
    recompor_endereco = endereco.split (' ')
    endereco = "/"
    for i in range (len(recompor_endereco) -1 ):
        if not endereco[-1] == '/':
            endereco = endereco + '/'
        endereco = endereco + recompor_endereco[i]
    entrada.delete(0, 10000)
    entrada.insert(0, endereco)
    clique_botao()

def clique_zip():
    import os 
    from zipfile import ZipFile, ZIP_DEFLATED

    nomesarquivos= os.listdir(diretorio)
    arquivo = os.listdir(diretorio)
    for nome in nomesarquivos:
        semextensao = nome.split('.')[0]
        nomezip = os.path.join(diretorio, semextensao + '.zip')
        arquivozip = ZipFile(nomezip,"w", compressao=ZIP_DEFLATED)
        arquivozip.write(os.path.join(diretorio, nome), nome)
        arquivozip.close()

    return len(nomearquivos)

if _name_ == '_main_':
    pasta = input("Digite o endereço da pasta ")
    print(f"Compactando arquivos em {pasta}")
    n = compactar_tudo(pasta)
    print(f"{n} arquivos compactados com sucesso")


janela = tkinter.Tk()

entrada = tkinter.Entry(janela)
botao = tkinter.Button(janela, command=clique_botao)
voltar = tkinter.Button(janela, command = clique_voltar, text = "...")
zipe = tkinter.Button(janela, command=clique_zip, text="ZIPAR")
lista_dir = tkinter.Listbox(janela, activestyle='dotbox',selectmode=tkinter.EXTENDED)
lista_dir.bind('<<ListboxSelect>>', selecionar_pasta)

entrada.insert(0, os.getcwd())
clique_botao()

entrada.pack(fill='both', expand=1)
botao.pack(fill='both', expand=1)
voltar.pack(fill='both', expand=1)
zipe.pack(fill='both', expand=1)
lista_dir.pack(fill='both', expand=1)
janela.mainloop()
