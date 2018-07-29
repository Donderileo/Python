#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#11 - Altere o programa anterior para mostrar a soma dos números.

x = int(input("Insira o número: "))
y = int(input("Insira o número: "))
soma = 0
if(y > x):
	for n in range(x+1,y):
		print(n)
		soma = soma + n
if(y < x):
	for n in range(y+1,x):
		print(n)
		soma = soma + n

print("A soma dos números presentes no intervalo é: %d"%soma)
