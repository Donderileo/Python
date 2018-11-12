def divide(lista):
	x = []
	y = []
	for i in range(0,len(lista),2): #for i in range(inicio,fim,intervalo)
		x.append(lista[i])
	for i in range(1,len(lista),2):
		y.append(lista[i])
	print("Nomes: ",x)
	print("Notas: ",y)

lista = ("Alberto", 15, "Leo", 18, "xyz", 123)
divide(lista) #Divide os nomes em uma lista de nomes, e as idades em uma lista de idades