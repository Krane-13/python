from tkinter import*

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

# fileira 0:
bt0 = Button(root, text="0", bg="lightgrey", pady=14, padx=38, bd=4, command= lambda: click_button(0))
bt0.place(x=5, y=265)
btPonto = Button(root, text=".", bg="lightgrey", pady=14, padx=15, bd=4, command=click_ponto) 
btPonto.place(x=101, y=265)

#fileira 1:
bt1 = Button(root, text="1", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(1))
bt1.place(x=5, y=210)

bt2 = Button(root, text="2", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(2))
bt2.place(x=52, y=210)

bt3 = Button(root, text="3", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(3))
bt3.place(x=100, y=210)

#fileira 2:
bt4 = Button(root, text="4", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(4))
bt4.place(x=5, y=155)

bt5 = Button(root, text="5", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(5))
bt5.place(x=52, y=155)

bt6 = Button(root, text="6", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(6))
bt6.place(x=100, y=155)

#fileira 3:
bt7 = Button(root, text="7", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(7))
bt7.place(x=5, y=100)

bt8 = Button(root, text="8", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(8))
bt8.place(x=52, y=100)

bt9 = Button(root, text="9", bg="lightgrey", pady=14, padx=14, bd=4, command= lambda: click_button(9))
bt9.place(x=100, y=100)

#operações:
btsoma = Button(root, text="+", bg="darkorange", pady=14, padx=14, bd=4, command=click_soma)
btsoma.place(x=148, y=100)

btsubtracao= Button(root, text="-", bg="darkorange", pady=14, padx=15, bd=4, command=click_sub)
btsubtracao.place(x=148, y=155)

btmultiplicacao = Button(root, text="X", bg="darkorange", pady=14, padx=14, bd=4, command=click_mult)
btmultiplicacao.place(x=148, y=210)

btdivi= Button(root, text="/", bg="darkorange", pady=14, padx=15, bd=4, command=click_div)
btdivi.place(x=148, y=265)

#botao de CE:
btce = Button(root, text="CE", bg="grey", pady=125, padx=15, bd=4, command=deletar)
btce.place(x=198, y=100)

#botao de igual:
btce = Button(root, text="=", bg="grey", pady=14, padx=85, bd=4, command=click_igual)
btce.place(x=5, y=322)

root.resizable(False, False)
root.geometry("280x380")
root.mainloop()