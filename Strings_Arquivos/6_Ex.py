arquivo = open("arquivo.txt","r")
texto = arquivo.read()
arquivo.close()

linhas = texto.splitlines()
print(linhas)

arquivo = open("arquivo.txt","w")
tamanho = len(linhas) - 1
for i in range(tamanho,-1,-1):
	arquivo.write(linhas[i])
	arquivo.write("\n")
arquivo.close()

arquivo = open("arquivo.txt","r")
print(arquivo.read())
arquivo.close()
