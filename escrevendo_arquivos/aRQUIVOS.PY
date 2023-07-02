#1)
#arquivo = open('Fim_Do_Mundo_Cecilia_Meireles.txt', 'r')
#arquivo = open('Copia-Fim_Do_Mundo_Cecilia_Meireles.txt', 'w')

#2)
# arquivo = open('Fim_Do_Mundo_Cecilia_Meireles.txt', 'r') 
# linha = arquivo.readlines()
    
# print(linha[0])
# print(linha[1])
# print(linha[2])
# print(linha[1])

#3)
# arquivo = open('Fim_Do_Mundo_Cecilia_Meireles.txt', 'r') 
# conteudo = arquivo.read()
# palavra = conteudo.split()

# arquivo_copia = open ('Copia-Fim_Do_Mundo_Cecilia_Meireles.txt', 'w')
# arquivo_copia.write(palavra + '\n')

#4)
# arquivo = open('Fim_Do_Mundo_Cecilia_Meireles.txt', 'r') 
# texto = arquivo.read()
    
# for letra in texto:
#     if letra == "":
#         break
#     print(letra)

#5)
arquivo = open('Fim_Do_Mundo_Cecilia_Meireles.txt', 'r') 
texto = arquivo.read()

texto_mod = texto.replace("o mundo", "a aula")

arquivo_copia = open('cronica_modificada.txt', 'w') 
arquivo_copia.write(texto_mod)