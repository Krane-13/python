from tkinter import *
import tkinter as tk

root = Tk()
root.title("Calculadora")


def click_igual():
    segundo_numero = visor.get()
    visor.delete(0,END)
    if matematica == "soma":
        visor.insert(0, p_numero + float(segundo_numero))
    if matematica == "subtracao":
        visor.insert(0, p_numero - float(segundo_numero))
    if matematica == "multiplicacao":
        visor.insert(0, p_numero * float(segundo_numero))
    if matematica == "divicao":
        visor.insert(0, p_numero / float(segundo_numero))

def click_soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "soma"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def click_sub():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "subtracao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def click_div():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "divicao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def click_mult():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "multiplicacao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def deletar():
    visor.delete(0,END)

def click_ponto():
    visor.insert(END,".")

def click_button(numero):
    atual = visor.get()
    visor.delete(0,END)
    visor.insert(END, str(atual) + str(numero))

lb1 = Label(text="CALCULADORA", font=("verdana", 20,"bold"), pady=10)
lb1.pack()
visor = Entry(root, bg="lightgrey")
visor.pack()

frame0 = tk.Frame(master= root, width=200, height=200)
frame0.pack()

frame1 = tk.Frame(master= root, width=150, height=150)
frame1.pack()
 
frame2 = tk.Frame(master=root, width=100, height=100)
frame2.pack()
 
frame3 = tk.Frame(master=root, width=50, height=50)
frame3.pack()

frame4 = tk.Frame(master=root, width=25, height=25)
frame4.pack()

frame5 = tk.Frame(master=root, width=0, height=0)
frame5.pack()
# fileira 0:
bt0 = Button(frame4, text="0", bg="lightgrey", pady=14, padx=38, bd=4, command= lambda: click_button(0))
bt0.pack(side = 'left')


#botao_1.pack(side = 'right', fill='both', expand=1)

btPonto = Button(frame4, text=".", bg="lightgrey", pady=14, padx=15, bd=4, command=click_ponto) 
#btPonto.place(x=101, y=265)
btPonto.pack(side='left')

#fileira 1:
bt1 = Button(frame3, text="1", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(1))
#bt1.place(x=5, y=210)
bt1.pack(side='left')

bt2 = Button(frame3, text="2", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(2))
#bt2.place(x=52, y=210)
bt2.pack(side='left')

bt3 = Button(frame3, text="3", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(3))
#bt3.place(x=100, y=210)
bt3.pack(side='left')

#fileira 2:
bt4 = Button(frame2, text="4", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(4))
#bt4.place(x=5, y=155)
bt4.pack(side='left')

bt5 = Button(frame2, text="5", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(5))
#bt5.place(x=52, y=155)
bt5.pack(side='left')

bt6 = Button(frame2, text="6", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(6))
# bt6.place(x=100, y=155)
bt6.pack(side='left')

#fileira 3:
bt7 = Button(frame1, text="7", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(7))
#bt7.place(x=5, y=100)
bt7.pack(side='left')

bt8 = Button(frame1, text="8", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(8))
# bt8.place(x=52, y=100)
bt8.pack(side='left')

bt9 = Button(frame1, text="9", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(9))
# bt9.place(x=100, y=100)
bt9.pack(side='left')

#operações:
btsoma = Button(frame4, text="+", bg="darkorange", pady=14, padx=14, bd=4, command=click_soma)
btsoma.pack(side='left')

btsubtracao= Button(frame3, text="-", bg="darkorange", pady=14, padx=15, bd=4, command=click_sub)
btsubtracao.pack(side='left')

btmultiplicacao = Button(frame2, text="X", bg="darkorange", pady=14, padx=14, bd=4, command=click_mult)
btmultiplicacao.pack(side='left')

btdivi= Button(frame1, text="/", bg="darkorange", pady=14, padx=15, bd=4, command=click_div)
btdivi.pack(side='left')

#botao de CE:
btce = Button(frame0, text="CE", bg="grey", pady=15, padx=80, bd=4, command=deletar)
btce.pack(side='right')

#botao de igual:
btce = Button(frame5, text="=", bg="grey", pady=14, padx=85, bd=4, command=click_igual)
btce.pack(side='left')

#root.resizable(False, False)
root.geometry("280x380")
root.mainloop()