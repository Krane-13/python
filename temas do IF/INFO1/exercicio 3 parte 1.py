nota1 = float(input('Digite sua 1º nota: '))
nota2 = float(input('Digite sua 2º nota: '))
nota3 = float(input('Digite sua 3º nota: '))
freq = int(input('Qual a frequencia do aluno? '))

media = (nota1 + nota2 + nota3) / 3
if media >= 7 and freq >= 75:
    print(f'A média foi de {media:.2f} e a frequencia foi de {freq}, aluno aprovado.')
else:
    print(f'A média foi de {media:.2f} e a frequencia foi de {freq}, aluno reprovado.')
    
