import tkinter
import Time
import random


time1 = Time.Time(1, "IFRS", ["Joao1", "Joao2", "Joao3"])
time2 = Time.Time(2, "IFGO", ["Maria1", "Maria2", "Maria3"])
time3 = Time.Time(3, "IFMA", ["Maria1", "Maria2", "Maria3"])
time4 = Time.Time(4, "IFPA", ["Maria1", "Maria2", "Maria3"])

lista_times = [time1, time2, time3, time4]
sorteio = lista_times

ind = random.randint (0,3)
print (sorteio[ind].nome + " contra")
lista_times.pop(ind)

ind = random.randint (0,2)
print (sorteio[ind].nome)
lista_times.pop(ind)
    


