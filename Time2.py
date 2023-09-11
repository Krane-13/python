import tkinter
import Time
import random

time1 = Time.Time(1, "IFRS", ["João1","João2","João3"])
time2 = Time.Time(2, "IFGO", ["Maria1","Maria2","Maria3"])
time3 = Time.Time(3, "IFMG", ["João1","João2","João3"])
time4 = Time.Time(4, "IFRJ", ["Maria1","Maria2","Maria3"])

lista_times = [time1, time2]
sorteio = lista_times

ind = random.randint(0,len(lista_times))
print(sorteio[ind].nome + "contra")
lista_times.pop(ind)

ind = random.randint(0,len(lista_times))
print(sorteio[ind].nome + "contra")
lista_times.pop(ind)


print(time1.jogadores)
print(time2.jogadores)

#print(lista_times[0].jogadores)
#print(lista_times[1].jogadores)
