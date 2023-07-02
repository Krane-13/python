a = int(input('Informe o valor de A: ')) #adicionar os valores
b = int(input('Informe o valor de B: '))
c = int(input('Informe o valor de C: '))

delta= b**2 - 4 * a * c # saber quando vale o delta
raiz= delta **0.5 # descobrir a raiz de delta
fase1=(-(b)+raiz)/(2*a) #calcular x¹
fase2=(-(b)-raiz)/(2*a) #calcular x²
print(f'O delta é: {delta}')
print(f'Com raiz igual: {raiz:.0f}')
print(f'x1 igual: {fase1:.2f}')
print(f'x2 igual: {fase2:.2f}')
if delta > 0:
    print('A função tem 2 raizes reais e diverentes')
elif delta == 0:
    print('A função tem 2 raizes reais e iguais')
else:
    print('A função NÃO possui raiz')

