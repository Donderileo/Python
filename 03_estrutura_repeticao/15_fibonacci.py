#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
anterior = 1
pre_anterior = 1
posicao = int(input("Escolha o termo: "))

if(posicao<=2):
	print("1")
else:
	for n in range(2,posicao):
			atual = anterior + pre_anterior
			pre_anterior = anterior
			anterior = atual

	print("O %d termo é: %d" %(posicao,atual))