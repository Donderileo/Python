#Python - Estrutura de Repetição
'''
numero = -1
while(numero>10 or numero < 0):
	numero = int(input("Insira um número: "))
'''
nome = 'a'
senha = 'a'
import os
erro = 0
while(nome == senha):
	if(erro == 1):
		print("ERRO TENTE NOVAMENTE")
	nome  = input("Insira nome:") 
	senha = input("Insira senha:")
	os.system('clear')
	erro = 1
	






