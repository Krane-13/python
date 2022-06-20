count = 0  # recebe o numero de pessasos que colocaram as notas
somanotas = 0 # vai receber o valor total das notas
while True:
    count +=1  # adiçona ao numero de pessoas
    nota = float(input('Digite sua nota: ')) # le a nota
    somanotas = somanotas + nota
    media =  somanotas / count # faz o calculo da media
    
    if nota== 0:  # condição de parada
        break
    
print(f'A media de notas é {media:.1f} ')
print(f'Tivemos a nota de {count -1} pessoas') # mostra só o numero de notas sem a nota negativa
