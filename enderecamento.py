import tkinter
import os

def botao():
    endereco = cleiton.get()
    conteudo = os.listdir(endereco)
    for i in range (len(conteudo)):
        lista_dir.insert(i, conteudo[i])
        
    #labelinho.config(text = os.listdir(endereco))
    

janela= tkinter.Tk()

cleiton = tkinter.Entry(janela)
cleiton_telas = tkinter.Button(janela, command=botao)
#labelinho = tkinter.Label(janela, text="conteudo da janela")
lista_dir = tkinter.Listbox(janela, activestyle='dotbox', selectmode=tkinter.EXTENDED)

cleiton.pack(fill='both', expand=1)
cleiton_telas.pack(fill='both', expand=1)
#labelinho.pack(fill='both', expand=1)
lista_dir.pack(fill='both', expand=1)
