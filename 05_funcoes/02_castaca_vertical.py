#numeros em cascata
def cascata(num):
	for i in range(1,num+2):
		j = 1
		while(j != i):
			print("%d"%(j),end=" ")
			j += 1

		print("\n")

		
num = int(input("Insira o número da cascata: "))
cascata(num)
