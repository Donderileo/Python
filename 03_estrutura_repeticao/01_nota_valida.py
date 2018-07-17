#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

numero = -1
while(numero>10 or numero < 0):
	numero = int(input("Insira um número: "))
