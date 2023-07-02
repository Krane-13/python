m = float(input("Massa: "))
a = float(input("Altura: "))

imc = m / (a**2) 
if imc < 18.5:
    print(f"{imc:.2f} Baixo")
elif imc > 18.5 and imc < 25:
    print(f"{imc:.2f} Normal")
else:
    print(f"{imc:.2f} Acima") 