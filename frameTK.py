import tkinter

def Funcao_1():
    texto.config (text = "1")
def Funcao_2():
    texto.config (text = "2")
def Funcao_3():
    texto.config (text = "3")
def Funcao_4():
    texto.config (text = "4")
def Funcao_5():
    texto.config (text = "5")
def Funcao_6():
    texto.config (text = "6")

janela = tkinter.Tk()
janela.geometry("300x300")
texto = tkinter.Label (janela, text="Ola Tk")

texto.pack(side='top')

quadro_1 = tkinter.Frame(janela)
quadro_2 = tkinter.Frame(janela)
quadro_3 = tkinter.Frame(janela)

botao_1 = tkinter.Button(quadro_1, command = Funcao_1, text='1')
botao_1.pack(side = 'right', fill='both', expand=1)
botao_2 = tkinter.Button(quadro_1, command = Funcao_2, text='1')
botao_2.pack(side = 'top', fill='both', expand=1)
botao_3 = tkinter.Button(quadro_2, command = Funcao_3, text='1')
botao_3.pack(side = 'top', fill='both', expand=1)
botao_4 = tkinter.Button(quadro_2, command = Funcao_4, text='1')
botao_4.pack(side = 'top', fill='both', expand=1)
botao_5 = tkinter.Button(quadro_3, command = Funcao_5, text='1')
botao_5.pack(side = 'top', fill='both', expand =1)
botao_6 = tkinter.Button(quadro_3, command = Funcao_6, text='1')
botao_6.pack(side = 'top', fill='both', expand =1)

quadro_1.pack(side='left', fill='both', expand=1)
quadro_2.pack(side='left', fill='both', expand=1)
quadro_3.pack(side='left', fill='both', expand=1)

janela.mainloop()
