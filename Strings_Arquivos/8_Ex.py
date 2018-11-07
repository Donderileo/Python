nl = int(input("Insira o número de linhas: "))
nc = int(input("Insira o número de colunas: "))
c = input("Escolha o caracter: ")
nome = input("Defina o nome do arquivo: ")

arquivo = open(nome,"w")
for i in range(0,nl):
	for j in range(0,nc):
		arquivo.write(" %c"%c)
	arquivo.write("\n")

arquivo.close()
arquivo = open(nome,"r")
print(arquivo.read())