#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
#Depois modifique o programa para que ele mostre os números um ao lado do outro.

#Um número por linha.
for n in range(1,21):
	print ("%d" %n)

#Todos números em uma linha só.
for n in range(1,21):
	print ("%d" %n,end=" ")