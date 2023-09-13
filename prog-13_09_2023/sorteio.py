import tkinter
import Time
import random

def registrar_jogador():
    nome = entry_nome_jogador.get()
    if not nome =="":
        lista_jogador.insert(tkinter.END, nome)

janela = tkinter.Tk()

label_desc_janela = tkinter.Label( text = "Janela de inscrição")
label_desc_nome = tkinter.Label(text = "Nome do Time")
label_desc_time = tkinter.Label(text = "Lista de jogadores")

entry_nome_time = tkinter.Entry()
lista_jogadores = tkinter.Listbox()
botao_pk = tkinter.Button(text = 'OK')

#teste cadastro
entry_nome_jogador = tkinter.entry()
botao_cadastro_jogador = tkinter.button(command = registrar_jogador)

label_desc_janela.grid(row=0, column=0)
lista_desc_nome.grid(row=1,column=0)
entry_nome_time.grid(row=1,column=1)

label_desc_nome.grid(row=2,column=0)
lista_jogadores.grid(row=2,column=1)

botao_ok.grid(row=3,column=1)

entry_nome_jogador.grid(row=4,column=)
botao_cadastro_jogador.grid(row=4,column=1)