#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
anterior = 1
pre_anterior = 1
atual = 0
print("1 1",end=" ")

while(atual<500):
		
		atual = anterior + pre_anterior
		pre_anterior = anterior
		anterior = atual
	
		if(atual < 500):
			print("%d" %atual,end=" ")