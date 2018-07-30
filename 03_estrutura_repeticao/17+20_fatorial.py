#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
number = 0
while(number != -1):
	resultado = 1

	number = int(input("Insira o número:         [-1] = Exit\n"))
	while(number>16):
		number = int(input("O número deve ser menor que 16!!\nInsira o número    [-1] - quit"))

	for n in range(number,1,-1):
		resultado = resultado * n

	print("Resultado do Fatorial: %d" %(resultado))