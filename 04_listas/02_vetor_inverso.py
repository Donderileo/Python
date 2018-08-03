#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []

for i in range(0,10):
	x = int(input("Insira o número: "))
	vetor.append(x)

print(vetor)
vetor.reverse()
print(vetor)