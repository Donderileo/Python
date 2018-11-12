nl = int(input("Insira o número de linhas: "))
nc = int(input("Insira o número de colunas: "))
c = input("Escolha o caracter: ")
nome = input("Defina o nome do arquivo: ")

arquivo = open(nome,"w")
for i in range(0,nl):#percorre as linhas
	for j in range(0,nc): #percorre as colunas
		arquivo.write(" %c"%c) #preenche com o caractere escolhido
	arquivo.write("\n") #pula linha quando encerra a ultima coluna

arquivo.close()
arquivo = open(nome,"r")
print(arquivo.read())