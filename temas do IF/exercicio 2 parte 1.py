distancia = float(input('Você quer correr quantos Km? '))
velocidade = int(input('Qual cera sua velocidade de corrida? '))
tempo = distancia / velocidade
minutos = tempo * 60
print(f'Se você for correr/camibhar {distancia} Km com uma velocidade de {velocidade} Km/h o seu tempo será de {tempo:.2f}h (ou {minutos:.2f} minutos)')
