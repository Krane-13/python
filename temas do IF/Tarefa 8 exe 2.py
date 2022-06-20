#Função para calcular o fatorial
def fatorial(n):
    f = 1
    for t in range(n,0,-1):
        f *= t
    return f
    

#Leitura do número que será feito o fatorial
n = int(input("Qual o fatorial de: "))

fator = fatorial(n) 
for a in range(n,0,-1): #mostrando de forma bonita como faz
    print(a, end='') 
    if a > 1:
        print(' X ',end='') 
    else:
         print(' = ',end='')
print(fator) #print do valor fatorial