#Faça um programa que leia 5 números e informe a soma e a média dos número
soma = 0
for n in range(1,6):
	soma = soma + int(input("Insira um número: "))

media = soma / n
print("Soma = %d" %soma)
print("Media = %.3f" %media)