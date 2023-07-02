countmale = countfamele = 0
while True:
    idade = int(input('Qual a sua idade: ')) # le idade 
    sexo =' ' 
    while sexo not in 'MF': #validação para apenas ecrever M ou F 
        sexo = str(input('Qual seu sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M' and idade < 20:
        countmale += 1 # contar homens com menos de 20 anos
    elif sexo == 'F':
        countfamele += 1 # contar o numero de mulheres
    escolha= ' '
    while escolha not in 'SN': #validação para apenas escrever S ou n
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N': #para loop quando escrever N
        break

print(f'O total de Homens com menos de 20 anos é de {countmale}') #mostrar ao user
print(f'O total de Mulheres é de {countfamele}')
