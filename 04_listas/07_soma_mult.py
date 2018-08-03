#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetor = []
mult = 1
for i in range(0,5):
	z = int(input("Insira um número: "))
	vetor.append(z)
	mult = mult * z

print ("Soma: ",end=" ")
print (sum(vetor))
print ("Multiplicação: %d"%(mult))

print ("Números: ",end=" ")
print (vetor)