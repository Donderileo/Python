#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.


def soma(a,b,c):
	return a+b+c

a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

resultado = soma(a,b,c)
print("Resultado: %d"%(resultado))