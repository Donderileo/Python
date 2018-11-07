def divide(lista):
	x = []
	y = []
	for i in range(0,len(lista),2):
		x.append(lista[i])
	for i in range(1,len(lista),2):
		y.append(lista[i])
	print("Nomes: ",x)
	print("Notas: ",y)

lista = ("Alberto", 15, "Leo", 18, "xyz", 123)
divide(lista)