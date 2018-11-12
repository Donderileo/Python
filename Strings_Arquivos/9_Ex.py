nl = int(input("Insira o número de linhas: "))
c = input("Escolha o caracter: ")
nome = input("Defina o nome do arquivo: ")

arquivo = open(nome,"w")
for i in  range(0,nl): #percorre todas as linhas
	for j in range (0,i+1): #percorre como número maximo, o numero de linhas +1 (dado que começamos na linha 0)
		arquivo.write(" %c"%c)
	arquivo.write("\n")

arquivo.close()
arquivo = open(nome,"r")
print(arquivo.read())