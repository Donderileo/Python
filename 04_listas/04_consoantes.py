#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []
vogais = ['a','e','i','o','u']

for i in range(0,10):
	x = input("Insira a letra: ")
	lista.append(x)

consoantes = []
cont = 0

for i in range(0,len(lista)):
	if  (lista[i] not in vogais):
		consoantes.append(lista[i])
		cont += 1

print("Você digitou %d consoantes"%(cont))
print (consoantes)

	