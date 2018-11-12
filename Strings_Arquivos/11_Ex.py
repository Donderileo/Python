def comparaArq(nome1,nome2):
	arquivo_1 = open(nome1,"r")
	arquivo_2 = open(nome2,"r")
	
	texto_1 = arquivo_1.read()
	texto_2 = arquivo_2.read()
	
	arquivo_1.close()
	arquivo_2.close()
	
	lista_x = texto_1.splitlines() #divide as duas strings por linhas em listas 
	lista_y = texto_2.splitlines()

	for i in range (0,len(lista_x)):
		for j in range (0,len(lista_y)):
			if(lista_x[i] == lista_y[j]): #procura para cada item da lista_x, algum da lista_y que seja identico
				return True
	return False

nome_1 = input("Insira o nome do arquivo 1: ")
nome_2 = input("Insira o nome do arquivo 2: ")
print(comparaArq(nome_1,nome_2))