n = int(input("Quantas notas você deseja cadastrar? "))
notas = list()
soma = 0
for c in range(1, n + 1):
    b = float(input(f"Sua nota na {c}° prova "))
    notas.append(b)
for nota in notas:
    soma += nota
    media = soma / n
print(soma)
print(media)
print(f"Teve um total de {n} cadastros de notas, a soma deu {soma:.1f} e a media é {media:.1f}")