valor = int(input('Qual valor em Doings você quer pagar? ')) #recebe valor

a = valor // 50
b = valor - 50 * a
c = b // 10
d = valor - 10 * c
e = valor - (50 * a + 10 * c) 
print(f'Valor solicidade foi {valor} pode ser pago com:')
print(f'{a} notas de 50')
print(f'{c} notas de 10')
print(f'{e} notas de 1')
