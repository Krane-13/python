receita = despesa = 0
quant = int(input('Digite um valor inteiro: '))
for c in range(1,quant+1):
    conta = float(input('Informe um valor: '))
    if conta < 0:
        despesa -= conta
    else:
        receita += conta
        
valor = receita - despesa
print(f'Sua receita é de R${valor:.2f}')
print(f'Sua receita era R${receita:.2f}')
print(f'Sua despesa era de -R${despesa:.2f}')
