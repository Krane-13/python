import zipfile

arquivo = zipfile.ZipFile("zipe.zip", mode="w")
arquivo.write ("teste.txt")
arquivo.write("/home/user/Desktop/Aulas_IF")

arquivo.write("/home/user/Desktop/Aulas_IF", "aulas_IF")
arquivo.close()
