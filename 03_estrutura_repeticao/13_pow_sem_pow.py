#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência
base = int(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))
resultado = 1
for n in range(0,expoente):
	resultado = base * resultado

print("Resultado: %d"%resultado)

