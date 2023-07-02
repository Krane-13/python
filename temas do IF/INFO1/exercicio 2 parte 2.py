valor = int(input('Qual valor em Doings você quer pagar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0 :
            print(f'Total de {totced} cédulas de Doings ${ced}')
        if ced == 50:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
if valor == 0:
    print("Não será necessario nenhuma cedula")      
        
            
        
