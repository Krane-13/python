from zipfile import ZipFile

with ZipFile("arquivo_compactado2.zip", "w") as zipagem:
    zipagem.write("Teste.txt")
    zipagem.write("Teste2.txt")

with ZipeFile("arquivo_compactado2.zip", "r") as zipagem:
    zipagem.extractall("destino")
