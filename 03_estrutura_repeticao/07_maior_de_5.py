#Faça um programa que leia 5 números e informe o maior número.

maior = int(input("Insira o número: "))
for n in range(1,5):

		x = int(input("Insira o número: "))
		if(x > maior):
				maior = x

print("Maior número: %d" %maior)