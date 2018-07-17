#02 - Faça um programa que leia um nome de usuário e a sua senha e 
#não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

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