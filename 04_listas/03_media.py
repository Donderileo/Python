#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
soma = 0

for i in range(0,4):
	x = int(input("Insira a nota: "))
	notas.append(x)
	soma = soma + x

print(notas)
media = soma /len(notas)
print("Media: %.2f"%(media))