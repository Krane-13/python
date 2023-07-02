import tkinter
import os

def selecionar_pasta(lista_dir):
    #pegar o que foi selecionado
    # criar o endereço do que foi selecionado
    #verificar se é uma pasta
    #acessar se foi uma pasta
    #senão, não faço nada
    novo_endereco =  entrada.get() + lista_dir()
    endereco = novo_endereco
    #filename = askopenfilename()
    try:
        conteudo = os.listdir(novo_endereco)
    except FileNotFoundError:
        lista_dir.insert(0, "Pasta nao encontrada")
    else:
        for i in range(len(conteudo)):
            lista_dir.insert(i, conteudo[i])
            
def clique_botao():
    lista_dir.delete(0, lista_dir.size())
    endereco = entrada.get()
    try:
        conteudo = os.listdir(endereco)
    except FileNotFoundError:
        lista_dir.insert(0, "Pasta nao encontrada")
    else:
        for i in range(len(conteudo)):
            lista_dir.insert(i, conteudo[i])


janela = tkinter.Tk()

entrada = tkinter.Entry(janela )
botao = tkinter.Button(janela, command=clique_botao)
lista_dir = tkinter.Listbox(janela, activestyle='dotbox',selectmode=tkinter.EXTENDED)
lista_dir.bind('<<ListboxSelect>>', selecionar_pasta)

entrada.pack(fill='both', expand=1)
botao.pack(fill='both', expand=1)
lista_dir.pack(fill='both', expand=1)
